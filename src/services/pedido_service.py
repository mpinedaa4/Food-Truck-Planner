from datetime import date

from fastapi import HTTPException, status

from data import mock_data
from schemas.pedido import (
    CanalPedido,
    DetallePedidoResponse,
    EstadoPedido,
    PedidoCreate,
    PedidoResponse,
    PedidoUpdate,
)

TRANSICIONES_ESTADO: dict[EstadoPedido, set[EstadoPedido]] = {
    EstadoPedido.RECIBIDO: {EstadoPedido.PREPARANDO, EstadoPedido.CANCELADO},
    EstadoPedido.PREPARANDO: {EstadoPedido.LISTO, EstadoPedido.CANCELADO},
    EstadoPedido.LISTO: {EstadoPedido.RECOGIDO, EstadoPedido.CANCELADO},
    EstadoPedido.RECOGIDO: set(),
    EstadoPedido.CANCELADO: set(),
}


def _validar_cliente(cliente_id: int) -> dict:
    cliente = mock_data.mock_clientes.get(cliente_id)
    if not cliente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Cliente con id {cliente_id} no encontrado",
        )
    return cliente


def _validar_camion(camion_id: int | None) -> None:
    if camion_id is not None and camion_id not in mock_data.mock_camiones:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Camión con id {camion_id} no encontrado",
        )


def _validar_productos(items: list) -> list[dict]:
    detalles = []
    for item in items:
        producto = mock_data.mock_productos.get(item.producto_id)
        if not producto:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Producto con id {item.producto_id} no encontrado",
            )
        detalles.append({
            "producto_id": item.producto_id,
            "cantidad": item.cantidad,
            "precio_unitario": producto["precio"],
        })
    return detalles


def _calcular_total(items: list[dict]) -> float:
    return sum(item["cantidad"] * item["precio_unitario"] for item in items)


def _construir_respuesta(pedido: dict) -> PedidoResponse:
    cliente = mock_data.mock_clientes[pedido["cliente_id"]]
    items_response = []
    for item in pedido["items"]:
        producto = mock_data.mock_productos[item["producto_id"]]
        subtotal = item["cantidad"] * item["precio_unitario"]
        items_response.append(DetallePedidoResponse(
            id=item["id"],
            producto_id=item["producto_id"],
            producto_nombre=producto["nombre"],
            cantidad=item["cantidad"],
            precio_unitario=item["precio_unitario"],
            subtotal=subtotal,
        ))
    return PedidoResponse(
        id=pedido["id"],
        cliente_id=pedido["cliente_id"],
        cliente_nombre=cliente["nombre"],
        camion_id=pedido["camion_id"],
        fecha_pedido=pedido["fecha_pedido"],
        hora_recogida=pedido["hora_recogida"],
        estado=EstadoPedido(pedido["estado"]),
        canal=CanalPedido(pedido["canal"]),
        total=_calcular_total(pedido["items"]),
        items=items_response,
    )


def _buscar_pedido(pedido_id: int) -> dict:
    for pedido in mock_data.mock_pedidos:
        if pedido["id"] == pedido_id:
            return pedido
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Pedido con id {pedido_id} no encontrado",
    )


def listar_pedidos(estado: EstadoPedido | None = None) -> list[PedidoResponse]:
    pedidos = mock_data.mock_pedidos
    if estado is not None:
        pedidos = [p for p in pedidos if p["estado"] == estado.value]
    return [_construir_respuesta(p) for p in pedidos]


def obtener_pedido(pedido_id: int) -> PedidoResponse:
    return _construir_respuesta(_buscar_pedido(pedido_id))


def crear_pedido(data: PedidoCreate) -> PedidoResponse:
    _validar_cliente(data.cliente_id)
    _validar_camion(data.camion_id)
    detalles = _validar_productos(data.items)

    items = []
    for detalle in detalles:
        items.append({
            "id": mock_data._next_detalle_id,
            "producto_id": detalle["producto_id"],
            "cantidad": detalle["cantidad"],
            "precio_unitario": detalle["precio_unitario"],
        })
        mock_data._next_detalle_id += 1

    pedido = {
        "id": mock_data._next_pedido_id,
        "cliente_id": data.cliente_id,
        "camion_id": data.camion_id,
        "fecha_pedido": date.today(),
        "hora_recogida": data.hora_recogida,
        "estado": EstadoPedido.RECIBIDO.value,
        "canal": data.canal.value,
        "items": items,
    }
    mock_data._next_pedido_id += 1
    mock_data.mock_pedidos.append(pedido)
    return _construir_respuesta(pedido)


def actualizar_pedido(pedido_id: int, data: PedidoUpdate) -> PedidoResponse:
    pedido = _buscar_pedido(pedido_id)

    if pedido["estado"] in (EstadoPedido.RECOGIDO.value, EstadoPedido.CANCELADO.value):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No se puede modificar un pedido recogido o cancelado",
        )

    if data.camion_id is not None:
        _validar_camion(data.camion_id)
        pedido["camion_id"] = data.camion_id

    if data.hora_recogida is not None:
        pedido["hora_recogida"] = data.hora_recogida

    return _construir_respuesta(pedido)


def actualizar_estado_pedido(pedido_id: int, nuevo_estado: EstadoPedido) -> PedidoResponse:
    pedido = _buscar_pedido(pedido_id)
    estado_actual = EstadoPedido(pedido["estado"])

    if nuevo_estado not in TRANSICIONES_ESTADO[estado_actual]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"No se puede cambiar de '{estado_actual.value}' a '{nuevo_estado.value}'",
        )

    pedido["estado"] = nuevo_estado.value
    return _construir_respuesta(pedido)


def cancelar_pedido(pedido_id: int) -> PedidoResponse:
    return actualizar_estado_pedido(pedido_id, EstadoPedido.CANCELADO)
