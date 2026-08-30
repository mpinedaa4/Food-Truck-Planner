# AGENTS.md

## Stack y comandos

- Python + FastAPI + Pydantic.
- Uvicorn para ejecutar la API y Pytest + HTTPX para pruebas.
- Dependencias: `requirements.txt`.
- Instalar: `pip install -r requirements.txt`
- Ejecutar: `uvicorn src.main:app --reload`
- Probar: `pytest`

## Estructura

- `src/main.py`: aplicación y registro de rutas.
- `src/data/mock_data.py`: datos mock en memoria.
- `src/services/`: lógica de negocio.
- `tests/`: pruebas.

Mantener separación entre rutas, servicios y datos. Seguir los patrones existentes antes de crear nuevas estructuras.

## API

- Usar rutas REST con recursos en plural.
- Pedidos:
  - `POST /pedidos`
  - `GET /pedidos`
  - `PATCH /pedidos/{id}/estado`
- `201` para creación exitosa.
- `200` para operaciones exitosas.
- `400` para entrada inválida o regla de negocio incumplida.
- `404` cuando el recurso no existe.
- Los errores deben ser JSON estructurado y consistente.
- Mantener respuestas JSON planas; no agregar envoltorios como `data` o `success` sin requerimiento explícito.

## Dominio

- Un `Pedido` representa una solicitud realizada a un food truck.
- Estados válidos: `Received`, `Preparing`, `Ready`, `Picked Up`.
- Una `Ruta` corresponde a un día y puede tener un camión asignado.
- Regla crítica: no se puede crear un pedido si para su fecha no existe una ruta con un camión asignado. En ese caso, rechazar con `400`.

## Pruebas

Los cambios de lógica de negocio deben incluir pruebas del caso exitoso y del caso de rechazo correspondiente.

## Restricciones

- No modificar `src/services/health_service.py`.
- No agregar base de datos real ni autenticación.
- No modificar frontend.
- No inventar recursos, campos, catálogos o funcionalidades que el requerimiento no necesite.
- No agregar dependencias sin necesidad; cualquier dependencia nueva debe declararse en `requirements.txt`.
- Mantener los cambios limitados al alcance solicitado.

## Convenciones

- Usar `snake_case` para archivos, funciones y variables.
- Ramas: `feature/<descripcion>`, `fix/<descripcion>`, `test/<descripcion>`.
- Commits: `<tipo>: <descripcion>` usando tipos como `feat`, `fix`, `test`, `docs` o `refactor`.
