from typing import Optional

from fastapi import HTTPException
from pydantic import BaseModel, Field

from data.mock_data import mock_orders, mock_routes

ORDER_STATUSES = ("Received", "Preparing", "Ready", "Picked Up")


class OrderItem(BaseModel):
    name: str
    quantity: int = Field(ge=1)


class CreateOrderRequest(BaseModel):
    customer_name: str
    customer_phone: str = ""
    items: list[OrderItem]
    pickup_date: str
    pickup_time: str = ""
    truck_id: int
    notes: str = ""


class UpdateOrderStatusRequest(BaseModel):
    status: str


def _next_order_id() -> int:
    if not mock_orders:
        return 1
    return max(order["id"] for order in mock_orders) + 1


def _route_with_assigned_truck(pickup_date: str, truck_id: int) -> bool:
    for route in mock_routes:
        if route.get("date") != pickup_date:
            continue
        assigned_truck = route.get("truck_id")
        if assigned_truck is None:
            continue
        if assigned_truck == truck_id:
            return True
    return False


def create_order(payload: CreateOrderRequest) -> dict:
    if not _route_with_assigned_truck(payload.pickup_date, payload.truck_id):
        raise HTTPException(
            status_code=400,
            detail=(
                "Cannot create an order: no route with an assigned truck "
                f"exists for date {payload.pickup_date} and truck {payload.truck_id}."
            ),
        )

    order = {
        "id": _next_order_id(),
        "customer_name": payload.customer_name,
        "customer_phone": payload.customer_phone,
        "items": [item.model_dump() for item in payload.items],
        "pickup_date": payload.pickup_date,
        "pickup_time": payload.pickup_time,
        "truck_id": payload.truck_id,
        "status": "Received",
        "notes": payload.notes,
    }
    mock_orders.append(order)
    return order


def list_orders(
    status: Optional[str] = None,
    date: Optional[str] = None,
    truck_id: Optional[int] = None,
) -> list[dict]:
    results = mock_orders
    if status is not None:
        results = [order for order in results if order["status"] == status]
    if date is not None:
        results = [order for order in results if order["pickup_date"] == date]
    if truck_id is not None:
        results = [order for order in results if order["truck_id"] == truck_id]
    return results


def update_order_status(order_id: int, payload: UpdateOrderStatusRequest) -> dict:
    if payload.status not in ORDER_STATUSES:
        raise HTTPException(
            status_code=400,
            detail=(
                f"Invalid status '{payload.status}'. "
                f"Must be one of: {', '.join(ORDER_STATUSES)}."
            ),
        )

    for order in mock_orders:
        if order["id"] == order_id:
            order["status"] = payload.status
            return order

    raise HTTPException(status_code=404, detail=f"Order {order_id} not found.")
