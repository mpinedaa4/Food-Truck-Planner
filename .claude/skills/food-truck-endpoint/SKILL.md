---
name: food-truck-endpoint
description: Agrega o modifica un endpoint REST del Food Truck Planner (FastAPI + Pydantic, datos mock en memoria) siguiendo AGENTS.md, con pruebas de éxito y de rechazo escritas antes del código. Úsala cuando pidan crear, cambiar o probar rutas de pedidos, rutas, camiones o inventario de este repositorio.
---

# Endpoint del Food Truck Planner

Adaptada de `fastapi-templates` (wshobson/agents, MIT) y `test-driven-development`
(obra/superpowers, MIT). Se eliminó todo lo que AGENTS.md prohíbe: base de datos,
SQLAlchemy, JWT, versionado `/api/v1` y dependencias nuevas.

`AGENTS.md` manda. Si algo de esta skill lo contradice, gana `AGENTS.md`.

## Antes de escribir código

1. Lee `AGENTS.md`, `src/main.py`, el servicio afectado en `src/services/` y `src/data/mock_data.py`.
2. Si existe una spec del cambio (`openspec/changes/<cambio>/` o `specs/<feature>/`), léela y toma de ahí los criterios de aceptación. Si no existe, pide los criterios antes de seguir.
3. Escribe en una lista corta: método y ruta, cuerpo o query params, respuesta exitosa, cada caso de rechazo con su código.

## Dónde va cada cosa

| Pieza | Archivo | Regla |
|---|---|---|
| Ruta | `src/main.py` | Solo recibe, llama al servicio y devuelve. Sin lógica de negocio. |
| Modelos de entrada | `src/services/<recurso>_service.py` | Pydantic v2, `Field` y `field_validator`, como `PedidoCreate`. |
| Lógica y reglas | `src/services/<recurso>_service.py` | Funciones en `snake_case`; lanzan `HTTPException` con `detail={"error": "..."}`. |
| Datos | `src/data/mock_data.py` | Listas en memoria. Nunca una base de datos real. |
| Pruebas | `tests/test_<recurso>.py` | `TestClient` de FastAPI, igual que `tests/test_pedidos.py`. |

No toques `src/services/health_service.py` ni el frontend.

## Contrato HTTP

- Recursos en plural: `/pedidos`, `/rutas`, `/camiones`.
- `201` al crear, `200` en lecturas y actualizaciones, `400` para entrada inválida o regla de negocio incumplida, `404` si el recurso no existe.
- Respuestas JSON planas, sin envoltorios `data` o `success`.
- Errores de reglas de negocio y `404` con la forma que usan los servicios: `{"detail": {"error": "<mensaje en español>"}}`. Ojo: los errores de validación de Pydantic salen por el handler de `main.py` como `{"error": ..., "detalle": [...]}`; en las pruebas verifica la forma que corresponda a cada caso y no unifiques ambas sin que la spec lo pida.
- Estados de pedido válidos: `Received`, `Preparing`, `Ready`, `Picked Up`.
- Regla crítica: no se crea un pedido si para su fecha no hay una ruta con camión asignado (`400`).

## Ciclo de trabajo (TDD)

Para cada comportamiento de la lista:

1. **Rojo.** Escribe una prueba del caso exitoso y una del caso de rechazo. Ejecuta `pytest tests/test_<recurso>.py -q` y confirma que fallan por la razón esperada (falta la ruta o la regla), no por un error de importación.
2. **Verde.** Escribe el mínimo código en servicio y ruta para que pasen.
3. **Suite completa.** Ejecuta `pytest -q`. Todo debe pasar, también las pruebas que no tocaste.
4. **Refactor** solo con la suite en verde.

Las pruebas no deben depender del orden: si una prueba modifica `mock_pedidos` u otra lista mock, restaura el estado (fixture con copia y restauración) o usa datos propios.

## Antes de decir que terminaste

- [ ] `pytest -q` corrido en este mismo paso, con 0 fallas (pega el resumen).
- [ ] Cada regla nueva tiene prueba de éxito y de rechazo.
- [ ] Ningún recurso, campo o dependencia que la spec no pida.
- [ ] `requirements.txt` sin cambios, o con la dependencia nueva justificada.
- [ ] Rama `feature/<descripcion>` y commits `<tipo>: <descripcion>` (`feat`, `fix`, `test`, `docs`, `refactor`).

## Qué no hacer

- No agregar autenticación, base de datos, CORS, middlewares ni versionado de API.
- No mover la lógica de negocio a `main.py`.
- No cambiar la forma de los errores existentes sin que la spec lo pida.
