from fastapi import FastAPI
from data.mock_data import mock_health_data
from services.health_service import get_health
from api.routes.pedidos import router as pedidos_router

app = FastAPI(
    title="Food Truck Planner API",
    description="API para gestionar pedidos y rutas de food trucks.",
    version="0.1.0",
)

app.include_router(pedidos_router, prefix="/pedidos", tags=["pedidos"])


@app.get("/")
def read_root():
    return mock_health_data


@app.get("/health")
def health():
    return get_health()
