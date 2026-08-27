mock_health_data = {
    "status": "ok"
}

ESTADOS_PEDIDO = ("Received", "Preparing", "Ready", "Picked Up")

mock_camiones = [
    {"id": 1, "nombre": "Truck A"},
    {"id": 2, "nombre": "Truck B"},
]

# Solo las rutas con camion_id distinto de None cuentan como camión asignado.
mock_rutas = [
    {"id": 1, "fecha": "2026-08-27", "camion_id": 1},
    {"id": 2, "fecha": "2026-08-28", "camion_id": 2},
    {"id": 3, "fecha": "2026-08-29", "camion_id": None},
]

mock_pedidos = [
    {
        "id": 1,
        "cliente": "Ana Pérez",
        "fecha": "2026-08-27",
        "camion_id": 1,
        "items": "2 tacos al pastor",
        "estado": "Received",
    }
]
