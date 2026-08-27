from fastapi import APIRouter, Query, status

from schemas.pedido import (
    EstadoPedido,
    EstadoPedidoUpdate,
    PedidoCreate,
    PedidoResponse,
    PedidoUpdate,
)
from services.pedido_service import (
    actualizar_estado_pedido,
    actualizar_pedido,
    cancelar_pedido,
    crear_pedido,
    listar_pedidos,
    obtener_pedido,
)

router = APIRouter()


@router.get("", response_model=list[PedidoResponse])
def get_pedidos(
    estado: EstadoPedido | None = Query(default=None, description="Filtrar por estado del pedido"),
):
    return listar_pedidos(estado=estado)


@router.get("/{pedido_id}", response_model=PedidoResponse)
def get_pedido(pedido_id: int):
    return obtener_pedido(pedido_id)


@router.post("", response_model=PedidoResponse, status_code=status.HTTP_201_CREATED)
def post_pedido(data: PedidoCreate):
    return crear_pedido(data)


@router.put("/{pedido_id}", response_model=PedidoResponse)
def put_pedido(pedido_id: int, data: PedidoUpdate):
    return actualizar_pedido(pedido_id, data)


@router.patch("/{pedido_id}/estado", response_model=PedidoResponse)
def patch_estado_pedido(pedido_id: int, data: EstadoPedidoUpdate):
    return actualizar_estado_pedido(pedido_id, data.estado)


@router.delete("/{pedido_id}", response_model=PedidoResponse)
def delete_pedido(pedido_id: int):
    return cancelar_pedido(pedido_id)
