from datetime import date
from typing import Optional

from fastapi import HTTPException
from pydantic import BaseModel, Field, field_validator

from data.mock_data import mock_pedidos, mock_rutas

ESTADOS_VALIDOS = ("Received", "Preparing", "Ready", "Picked Up")


class PedidoCreate(BaseModel):
    fecha: date
    camion_id: int = Field(..., gt=0)
    cliente: str = Field(..., min_length=1)
    items: list[str] = Field(..., min_length=1)

    @field_validator("cliente")
    @classmethod
    def cliente_no_vacio(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("cliente es requerido")
        return value

    @field_validator("items")
    @classmethod
    def items_no_vacios(cls, value: list[str]) -> list[str]:
        limpios = [item.strip() for item in value if item and item.strip()]
        if not limpios:
            raise ValueError("items debe incluir al menos un producto")
        return limpios


class PedidoEstadoUpdate(BaseModel):
    estado: str = Field(..., min_length=1)

    @field_validator("estado")
    @classmethod
    def estado_valido(cls, value: str) -> str:
        if value not in ESTADOS_VALIDOS:
            raise ValueError(
                "estado debe ser uno de: Received, Preparing, Ready, Picked Up"
            )
        return value


def _ruta_con_camion_asignado(fecha: str, camion_id: int) -> bool:
    for ruta in mock_rutas:
        if (
            ruta["fecha"] == fecha
            and ruta["camion_id"] is not None
            and ruta["camion_id"] == camion_id
        ):
            return True
    return False


def _siguiente_id() -> int:
    if not mock_pedidos:
        return 1
    return max(pedido["id"] for pedido in mock_pedidos) + 1


def create_pedido(payload: PedidoCreate) -> dict:
    fecha = payload.fecha.isoformat()
    if not _ruta_con_camion_asignado(fecha, payload.camion_id):
        raise HTTPException(
            status_code=400,
            detail={
                "error": (
                    "No se puede crear el pedido: no existe una ruta "
                    "con un camión asignado para esa fecha"
                )
            },
        )

    pedido = {
        "id": _siguiente_id(),
        "fecha": fecha,
        "camion_id": payload.camion_id,
        "cliente": payload.cliente,
        "items": payload.items,
        "estado": "Received",
    }
    mock_pedidos.append(pedido)
    return pedido


def list_pedidos(
    estado: Optional[str] = None,
    fecha: Optional[str] = None,
    camion: Optional[int] = None,
) -> list[dict]:
    if estado is not None and estado not in ESTADOS_VALIDOS:
        raise HTTPException(
            status_code=400,
            detail={
                "error": (
                    "estado debe ser uno de: Received, Preparing, Ready, Picked Up"
                )
            },
        )

    if fecha is not None:
        try:
            date.fromisoformat(fecha)
        except ValueError as exc:
            raise HTTPException(
                status_code=400,
                detail={"error": "fecha debe tener formato YYYY-MM-DD"},
            ) from exc

    resultados = mock_pedidos
    if estado is not None:
        resultados = [pedido for pedido in resultados if pedido["estado"] == estado]
    if fecha is not None:
        resultados = [pedido for pedido in resultados if pedido["fecha"] == fecha]
    if camion is not None:
        resultados = [pedido for pedido in resultados if pedido["camion_id"] == camion]
    return resultados


def update_pedido_estado(pedido_id: int, payload: PedidoEstadoUpdate) -> dict:
    for pedido in mock_pedidos:
        if pedido["id"] == pedido_id:
            pedido["estado"] = payload.estado
            return pedido
    raise HTTPException(
        status_code=404,
        detail={"error": "Pedido no encontrado"},
    )
