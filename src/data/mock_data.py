mock_health_data = {
    "status": "ok"
}

# Two Street Corner Eats trucks. Orders can only be created for a date
# that already has a route with a truck assigned.
mock_trucks = [
    {"id": 1, "name": "Taco Tornado"},
    {"id": 2, "name": "Burger Boulevard"},
]

mock_routes = [
    {
        "id": 1,
        "date": "2026-08-27",
        "truck_id": 1,
        "stops": ["Downtown Plaza", "University Campus"],
    },
    {
        "id": 2,
        "date": "2026-08-27",
        "truck_id": 2,
        "stops": ["Riverside Park", "Tech District"],
    },
    {
        "id": 3,
        "date": "2026-08-28",
        "truck_id": 1,
        "stops": ["City Hall"],
    },
    {
        "id": 4,
        "date": "2026-08-29",
        "truck_id": None,
        "stops": ["Market Square"],
    },
]

mock_orders = [
    {
        "id": 1,
        "customer_name": "Ana Ruiz",
        "customer_phone": "555-0101",
        "items": [{"name": "Taco al pastor", "quantity": 2}],
        "pickup_date": "2026-08-27",
        "pickup_time": "12:30",
        "truck_id": 1,
        "status": "Received",
        "notes": "",
    },
]
