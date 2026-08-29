import pytest
from fastapi.testclient import TestClient

from data.mock_data import mock_pedidos
from src.main import app

client = TestClient(app)


@pytest.fixture(autouse=True)
def restore_pedidos():
    original = [pedido.copy() for pedido in mock_pedidos]
    yield
    mock_pedidos.clear()
    mock_pedidos.extend(original)


def test_crear_pedido_feliz():
    response = client.post(
        "/pedidos",
        json={
            "fecha": "2026-08-28",
            "camion_id": 1,
            "cliente": "Luis Gomez",
            "items": ["Quesadilla"],
        },
    )

    assert response.status_code == 201
    body = response.json()
    assert body["cliente"] == "Luis Gomez"
    assert body["estado"] == "Received"
    assert body["fecha"] == "2026-08-28"
    assert body["camion_id"] == 1


def test_crear_pedido_falla_sin_ruta_con_camion_asignado():
    response = client.post(
        "/pedidos",
        json={
            "fecha": "2026-08-30",
            "camion_id": 1,
            "cliente": "Luis Gomez",
            "items": ["Quesadilla"],
        },
    )

    assert response.status_code == 400
    body = response.json()
    assert "error" in body["detail"]
    assert "ruta" in body["detail"]["error"].lower()


def test_crear_pedido_falla_si_ruta_existe_sin_camion():
    response = client.post(
        "/pedidos",
        json={
            "fecha": "2026-08-29",
            "camion_id": 1,
            "cliente": "Luis Gomez",
            "items": ["Quesadilla"],
        },
    )

    assert response.status_code == 400
    assert "error" in response.json()["detail"]


def test_listar_pedidos_filtra_por_estado_fecha_y_camion():
    response = client.get(
        "/pedidos",
        params={"estado": "Received", "fecha": "2026-08-28", "camion": 1},
    )

    assert response.status_code == 200
    body = response.json()
    assert isinstance(body, list)
    assert len(body) >= 1
    assert all(
        pedido["estado"] == "Received"
        and pedido["fecha"] == "2026-08-28"
        and pedido["camion_id"] == 1
        for pedido in body
    )


def test_cambiar_estado_pedido_y_404_si_no_existe():
    update = client.patch("/pedidos/1/estado", json={"estado": "Preparing"})
    assert update.status_code == 200
    assert update.json()["estado"] == "Preparing"

    missing = client.patch("/pedidos/999/estado", json={"estado": "Ready"})
    assert missing.status_code == 404
    assert "error" in missing.json()["detail"]
