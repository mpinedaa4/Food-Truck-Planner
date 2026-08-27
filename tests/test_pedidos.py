import sys
from pathlib import Path

src_dir = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(src_dir))

from fastapi.testclient import TestClient

from data.mock_data import mock_pedidos
from main import app

client = TestClient(app)


def test_health_sigue_disponible():
    respuesta = client.get("/health")
    assert respuesta.status_code == 200
    assert respuesta.json() == {"status": "ok"}

PEDIDO_VALIDO = {
    "cliente": "Carlos Ruiz",
    "fecha": "2026-08-27",
    "camion_id": 1,
    "items": "1 burrito",
}


def test_crear_pedido_sin_ruta_con_camion_asignado_debe_fallar():
    cantidad_antes = len(mock_pedidos)
    respuesta = client.post(
        "/pedidos",
        json={
            "cliente": "Luis Soto",
            "fecha": "2026-08-29",
            "camion_id": 1,
            "items": "3 quesadillas",
        },
    )

    assert respuesta.status_code == 400
    cuerpo = respuesta.json()
    assert cuerpo == {"error": "No hay ruta con un camión asignado para esa fecha"}
    assert len(mock_pedidos) == cantidad_antes


def test_crear_pedido_con_ruta_y_camion_asignado_debe_crear():
    cantidad_antes = len(mock_pedidos)
    respuesta = client.post("/pedidos", json=PEDIDO_VALIDO)

    assert respuesta.status_code == 200
    cuerpo = respuesta.json()
    assert cuerpo["cliente"] == PEDIDO_VALIDO["cliente"]
    assert cuerpo["fecha"] == PEDIDO_VALIDO["fecha"]
    assert cuerpo["camion_id"] == PEDIDO_VALIDO["camion_id"]
    assert cuerpo["items"] == PEDIDO_VALIDO["items"]
    assert cuerpo["estado"] == "Received"
    assert "id" in cuerpo
    assert len(mock_pedidos) == cantidad_antes + 1


def test_pedido_inexistente_devuelve_404():
    respuesta = client.patch("/pedidos/99999/estado", json={"estado": "Preparing"})

    assert respuesta.status_code == 404
    assert respuesta.json() == {"error": "Pedido no encontrado"}
