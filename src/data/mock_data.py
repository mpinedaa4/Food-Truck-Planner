from datetime import date, datetime

mock_health_data = {
    "status": "ok"
}

mock_clientes = {
    1: {"id": 1, "nombre": "María García", "telefono": "3001234567", "email": "maria@email.com"},
    2: {"id": 2, "nombre": "Carlos López", "telefono": "3109876543", "email": "carlos@email.com"},
    3: {"id": 3, "nombre": "Ana Rodríguez", "telefono": "3205551234", "email": "ana@email.com"},
}

mock_productos = {
    1: {"id": 1, "nombre": "Hamburguesa clásica", "descripcion": "Carne, lechuga, tomate", "precio": 15000.0, "categoria": "hamburguesas"},
    2: {"id": 2, "nombre": "Perro caliente", "descripcion": "Salchicha, salsas", "precio": 8000.0, "categoria": "perros"},
    3: {"id": 3, "nombre": "Papas fritas", "descripcion": "Porción mediana", "precio": 5000.0, "categoria": "acompañantes"},
    4: {"id": 4, "nombre": "Limonada natural", "descripcion": "Vaso 500ml", "precio": 4000.0, "categoria": "bebidas"},
}

mock_camiones = {
    1: {"id": 1, "nombre": "Food Truck Norte", "placa": "ABC123", "estado": "activo"},
    2: {"id": 2, "nombre": "Food Truck Sur", "placa": "DEF456", "estado": "activo"},
}

mock_pedidos = [
    {
        "id": 1,
        "cliente_id": 1,
        "camion_id": 1,
        "fecha_pedido": date(2026, 8, 27),
        "hora_recogida": datetime(2026, 8, 27, 12, 30),
        "estado": "recibido",
        "canal": "telefono",
        "items": [
            {"id": 1, "producto_id": 1, "cantidad": 2, "precio_unitario": 15000.0},
            {"id": 2, "producto_id": 3, "cantidad": 1, "precio_unitario": 5000.0},
        ],
    },
    {
        "id": 2,
        "cliente_id": 2,
        "camion_id": 1,
        "fecha_pedido": date(2026, 8, 27),
        "hora_recogida": datetime(2026, 8, 27, 13, 0),
        "estado": "preparando",
        "canal": "redes_sociales",
        "items": [
            {"id": 3, "producto_id": 2, "cantidad": 3, "precio_unitario": 8000.0},
            {"id": 4, "producto_id": 4, "cantidad": 2, "precio_unitario": 4000.0},
        ],
    },
]

_next_pedido_id = 3
_next_detalle_id = 5
