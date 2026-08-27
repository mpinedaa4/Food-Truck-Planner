from datetime import datetime

from pydantic import BaseModel, Field, field_validator

from data.mock_data import ESTADOS_PEDIDO, mock_pedidos, mock_rutas


class PedidoError(Exception):
    def __init__(self, mensaje, codigo_http=400):
        super().__init__(mensaje)
        self.mensaje = mensaje
        self.codigo_http = codigo_http


class PedidoCreate(BaseModel):
    cliente: str = Field(..., min_length=1)
    fecha: str
    camion_id: int
    items: str = Field(..., min_length=1)

    @field_validator("cliente", "items")
    @classmethod
    def no_solo_espacios(cls, valor):
        if not valor.strip():
            raise ValueError("no puede estar vacío")
        return valor.strip()

    @field_validator("fecha")
    @classmethod
    def fecha_yyyy_mm_dd(cls, valor):
        try:
            datetime.strptime(valor, "%Y-%m-%d")
        except (TypeError, ValueError) as exc:
            raise ValueError("debe tener formato YYYY-MM-DD") from exc
        return valor


class EstadoUpdate(BaseModel):
    estado: str = Field(..., min_length=1)

    @field_validator("estado")
    @classmethod
    def estado_permitido(cls, valor):
        if valor not in ESTADOS_PEDIDO:
            permitidos = ", ".join(ESTADOS_PEDIDO)
            raise ValueError(f"debe ser uno de: {permitidos}")
        return valor


def hay_ruta_con_camion_asignado(fecha, camion_id):
    for ruta in mock_rutas:
        if (
            ruta.get("fecha") == fecha
            and ruta.get("camion_id") is not None
            and ruta.get("camion_id") == camion_id
        ):
            return True
    return False


def _siguiente_id():
    if not mock_pedidos:
        return 1
    return max(pedido["id"] for pedido in mock_pedidos) + 1


def crear_pedido(datos: PedidoCreate):
    if not hay_ruta_con_camion_asignado(datos.fecha, datos.camion_id):
        raise PedidoError(
            "No hay ruta con un camión asignado para esa fecha",
            codigo_http=400,
        )

    pedido = {
        "id": _siguiente_id(),
        "cliente": datos.cliente,
        "fecha": datos.fecha,
        "camion_id": datos.camion_id,
        "items": datos.items,
        "estado": "Received",
    }
    mock_pedidos.append(pedido)
    return pedido


def listar_pedidos(estado=None, fecha=None, camion=None):
    if fecha is not None:
        try:
            datetime.strptime(fecha, "%Y-%m-%d")
        except (TypeError, ValueError) as exc:
            raise PedidoError("La fecha debe tener formato YYYY-MM-DD") from exc

    if estado is not None and estado not in ESTADOS_PEDIDO:
        permitidos = ", ".join(ESTADOS_PEDIDO)
        raise PedidoError(f"El estado debe ser uno de: {permitidos}")

    resultados = mock_pedidos
    if estado is not None:
        resultados = [p for p in resultados if p["estado"] == estado]
    if fecha is not None:
        resultados = [p for p in resultados if p["fecha"] == fecha]
    if camion is not None:
        resultados = [p for p in resultados if p["camion_id"] == camion]
    return resultados


def cambiar_estado(pedido_id, datos: EstadoUpdate):
    for pedido in mock_pedidos:
        if pedido["id"] == pedido_id:
            pedido["estado"] = datos.estado
            return pedido
    raise PedidoError("Pedido no encontrado", codigo_http=404)
