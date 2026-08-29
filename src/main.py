import sys
from pathlib import Path
from typing import Optional

_SRC_DIR = Path(__file__).resolve().parent
if str(_SRC_DIR) not in sys.path:
    sys.path.insert(0, str(_SRC_DIR))

from fastapi import FastAPI, Query
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from data.mock_data import mock_health_data
from services.health_service import get_health
from services.pedido_service import (
    PedidoCreate,
    PedidoEstadoUpdate,
    create_pedido,
    list_pedidos,
    update_pedido_estado,
)

app = FastAPI(
    title="FastAPI Starter",
    description="Baseline FastAPI project.",
    version="0.1.0",
)


@app.exception_handler(RequestValidationError)
def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content={"error": "Datos inválidos", "detalle": exc.errors()},
    )


@app.get("/")
def read_root():
    return mock_health_data


@app.get("/health")
def health():
    return get_health()


@app.post("/pedidos", status_code=201)
def crear_pedido(pedido: PedidoCreate):
    return create_pedido(pedido)


@app.get("/pedidos")
def obtener_pedidos(
    estado: Optional[str] = Query(default=None),
    fecha: Optional[str] = Query(default=None),
    camion: Optional[int] = Query(default=None),
):
    return list_pedidos(estado=estado, fecha=fecha, camion=camion)


@app.patch("/pedidos/{id}/estado")
def cambiar_estado_pedido(id: int, payload: PedidoEstadoUpdate):
    return update_pedido_estado(id, payload)
