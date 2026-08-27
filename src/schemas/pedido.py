from datetime import date, datetime
from enum import Enum

from pydantic import BaseModel, Field


class EstadoPedido(str, Enum):
    RECIBIDO = "recibido"
    PREPARANDO = "preparando"
    LISTO = "listo"
    RECOGIDO = "recogido"
    CANCELADO = "cancelado"


class CanalPedido(str, Enum):
    TELEFONO = "telefono"
    REDES_SOCIALES = "redes_sociales"
    WEB = "web"
    PRESENCIAL = "presencial"


class DetallePedidoCreate(BaseModel):
    producto_id: int = Field(..., gt=0)
    cantidad: int = Field(..., gt=0)


class PedidoCreate(BaseModel):
    cliente_id: int = Field(..., gt=0)
    camion_id: int | None = Field(default=None, gt=0)
    hora_recogida: datetime
    canal: CanalPedido
    items: list[DetallePedidoCreate] = Field(..., min_length=1)


class PedidoUpdate(BaseModel):
    camion_id: int | None = Field(default=None, gt=0)
    hora_recogida: datetime | None = None


class EstadoPedidoUpdate(BaseModel):
    estado: EstadoPedido


class DetallePedidoResponse(BaseModel):
    id: int
    producto_id: int
    producto_nombre: str
    cantidad: int
    precio_unitario: float
    subtotal: float


class PedidoResponse(BaseModel):
    id: int
    cliente_id: int
    cliente_nombre: str
    camion_id: int | None
    fecha_pedido: date
    hora_recogida: datetime
    estado: EstadoPedido
    canal: CanalPedido
    total: float
    items: list[DetallePedidoResponse]
