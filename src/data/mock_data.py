mock_health_data = {
    "status": "ok"
}

mock_camiones = [
    {"id": 1, "nombre": "Street Corner Eats 1"},
    {"id": 2, "nombre": "Street Corner Eats 2"},
]

mock_rutas = [
    {
        "id": 1,
        "fecha": "2026-08-28",
        "camion_id": 1,
    },
    {
        "id": 2,
        "fecha": "2026-08-28",
        "camion_id": 2,
    },
    {
        "id": 3,
        "fecha": "2026-08-29",
        "camion_id": None,
    },
]

mock_pedidos = [
    {
        "id": 1,
        "fecha": "2026-08-28",
        "camion_id": 1,
        "cliente": "Ana Perez",
        "items": ["Taco de pastor", "Agua"],
        "estado": "Received",
    }
]
