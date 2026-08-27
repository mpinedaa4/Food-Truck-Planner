from pathlib import Path
import sys

from typing import Optional

from fastapi import FastAPI, Query
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

src_dir = Path(__file__).resolve().parent
if str(src_dir) not in sys.path:
    sys.path.insert(0, str(src_dir))

from data.mock_data import mock_health_data
from services.health_service import get_health
from services.pedido_service import (
    EstadoUpdate,
    PedidoCreate,
    PedidoError,
    cambiar_estado,
    crear_pedido,
    listar_pedidos,
)

app = FastAPI(
    title="FastAPI Starter",
    description="Baseline FastAPI project.",
    version="0.1.0",
)


@app.exception_handler(RequestValidationError)
async def manejar_validacion(request, exc):
    return JSONResponse(status_code=400, content={"error": "Datos inválidos"})


@app.exception_handler(PedidoError)
async def manejar_pedido_error(request, exc):
    return JSONResponse(status_code=exc.codigo_http, content={"error": exc.mensaje})


@app.get("/")
def read_root():
    return mock_health_data


@app.get("/health")
def health():
    return get_health()


@app.post("/pedidos")
def post_pedidos(datos: PedidoCreate):
    return crear_pedido(datos)


@app.get("/pedidos")
def get_pedidos(
    estado: Optional[str] = Query(default=None),
    fecha: Optional[str] = Query(default=None),
    camion: Optional[int] = Query(default=None),
):
    return listar_pedidos(estado=estado, fecha=fecha, camion=camion)


@app.patch("/pedidos/{pedido_id}/estado")
def patch_pedido_estado(pedido_id: int, datos: EstadoUpdate):
    return cambiar_estado(pedido_id, datos)
