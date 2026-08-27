from typing import Optional

from fastapi import FastAPI
from data.mock_data import mock_health_data
from services.health_service import get_health
from services.order_service import (
    CreateOrderRequest,
    UpdateOrderStatusRequest,
    create_order,
    list_orders,
    update_order_status,
)

app = FastAPI(
    title="FastAPI Starter",
    description="Baseline FastAPI project.",
    version="0.1.0",
)


@app.get("/")
def read_root():
    return mock_health_data


@app.get("/health")
def health():
    return get_health()


@app.post("/orders", status_code=201)
def post_order(payload: CreateOrderRequest):
    return create_order(payload)


@app.get("/orders")
def get_orders(
    status: Optional[str] = None,
    date: Optional[str] = None,
    truck_id: Optional[int] = None,
):
    return list_orders(status=status, date=date, truck_id=truck_id)


@app.patch("/orders/{order_id}/status")
def patch_order_status(order_id: int, payload: UpdateOrderStatusRequest):
    return update_order_status(order_id, payload)