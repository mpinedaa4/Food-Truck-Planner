# Prompt V1

## Prompt

Haz el endpoint de pedidos para el food truck planner, desarrollaras una app para gestionar los sitemas de pedido de un foodtruck el genera una ruta en base a pedidos previos.

## Criterios de verificación

1. Comando de arranque documentado: No cumple
2. Convención REST declarada: No cumple
3. Regla de negocio del RFP implementada: No cumple
4. Validación y errores estructurados: Cumple
5. Respeta estructura y nombres de referencia: No cumple
6. Mantiene formato de respuesta de referencia: No cumple
7. Incluye prueba de la regla de negocio: No cumple
8. Dependencias declaradas en el manifiesto: Cumple

**Total cumplidos:** 2 de 8

## Alucinaciones

Se identificaron 15 elementos generados o inferidos sin estar explícitamente solicitados o respaldados por el prompt original:

1. Estructura de carpetas (api/routes/, schemas/).
2. Seis operaciones CRUD (GET, POST, PUT, PATCH, DELETE).
3. Ruta /pedidos.
4. Estados (recibido, preparando, listo, recogido, cancelado).
5. Canales (telefono, redes_sociales, web, presencial).
6. Campos adicionales (cliente_id, camion_id, hora_recogida, canal, items, etc.).
7. Datos mock de clientes, productos y camiones.
8. Pedidos de ejemplo con fechas específicas.
9. Máquina de transiciones de estado.
10. Bloqueo de edición para pedidos recogido/cancelado.
11. DELETE interpretado como cancelación lógica.
12. Validaciones de existencia sobre catálogos mock.
13. Formato de respuesta enriquecido (PedidoResponse).
14. Cambio del título de la API a "Food Truck Planner API".
15. Vínculo entre pedidos y rutas, mencionado pero no implementado.

> **Nota:** algunos elementos estaban respaldados por documentación existente en el repositorio (MVP, ERD, etc.), pero dicha documentación no formaba parte del prompt evaluado.

## Conclusión

El prompt original presenta baja efectividad frente a los 8 criterios de verificación. Es demasiado general y no proporciona información suficiente sobre aspectos esenciales como la convención REST, estructura de referencia, formato de respuesta, reglas de negocio, pruebas y documentación de ejecución.

Esto provocó que la IA sobre-especificara elementos no solicitados (CRUD completo, estructuras, estados y datos mock) mientras que omitió aspectos importantes del dominio, especialmente la relación entre pedidos y rutas.

# Prompt V2

## Prompt

Eres un desarrollador backend trabajando en el proyecto Food Truck Planner,
una API en FastAPI para Street Corner Eats (dos food trucks que reciben
pre-pedidos y necesitan coordinar rutas diarias).

OBJETIVO
Cuando termines debe existir en el backend:

1. Un endpoint para crear un pedido.
2. Un endpoint para listar pedidos, con filtro por estado, fecha y camión.
3. Un endpoint para cambiar el estado de un pedido (Received, Preparing,
   Ready, Picked Up).

CONTEXTO

- El proyecto vive en /src, usa FastAPI, y no tiene base de datos real
  todavía: los datos se guardan en constantes de Python en memoria,
  dentro de src/data/mock_data.py.
- La lógica de cada recurso vive en un archivo de servicio dentro de
  src/services/, y las rutas se registran en src/main.py.
- Ya existe un recurso de ejemplo (health) siguiendo este patrón.
- Regla de negocio obligatoria: no se puede crear un pedido para una
  fecha si no existe una ruta con un camión ya asignado para ese día.
  Si no existe esa ruta, el pedido debe rechazarse.

ALCANCE

- Sí puedes: crear/editar archivos dentro de src/data/ y src/services/,
  y agregar las nuevas rutas a src/main.py.
- No toques: src/services/health_service.py, no agregues base de
  datos real, no agregues autenticación, no toques nada de frontend.

## Criterios de verificación

1. Arranca con un solo comando y está documentado: Parcialmente (no está documentado)
2. Uso de convención REST: Cumple
3. Implementa la regla de negocio del RFP: Cumple
4. Valida la entrada y devuelve errores estructurados: Cumple
5. Respeta estructura de carpetas y nombres de archivo: Cumple
6. Devuelve el mismo formato de respuesta que el archivo de referencia: Cumple
7. Incluye al menos una prueba que ejercita la regla de negocio: No cumple
8. Todas las dependencias existen y están declaradas: Cumple

**Total cumplidos:** 6 de 8

## Alucinaciones

En esta versión la IA no generó ninguna alucinación. Creo los archivos correctos y usó todas las funciones que generó de manera correcta. No creó funciones o código que no se le haya solicitado de manera explícita. Aunque tuvo mayor libertad a la hora de crear los datos mock, todos los datos que creó eran pertinentes para las nuevas funciones y seguían las reglas de negocio.

## Conclusión

Al agregar el rol, objetivo y restricciones al prompt mejoramos el output de la IA, con una estructura de archivos y carpetas similares a lo que queremos, siguiendo adecuadamente las reglas de negocio que le detallamos en el objetivo. Sigue siendo una implementación muy básica que podría mejorar en algunos aspectos, siendo esto evidenciado en los 8 criterios de verificación.

Podemos ver, entonces, que una mejor definición del prompt, con más elementos y contexto para la IA puiede mejorar significativamente el resultado obtenido, por lo que esperamos que en la versión 3 y 4 el resultado sea aún más refinado.

# Prompt V3

## Prompt

V3 — + Criterios de aceptación y formato de salida
Eres un desarrollador backend trabajando en el proyecto Food Truck Planner,
una API en FastAPI para Street Corner Eats (dos food trucks que reciben
pre-pedidos y necesitan coordinar rutas diarias).

OBJETIVO
Cuando termines debe existir en el backend:

1. Un endpoint para crear un pedido.
2. Un endpoint para listar pedidos, con filtro por estado, fecha y camión.
3. Un endpoint para cambiar el estado de un pedido (Received, Preparing,
   Ready, Picked Up).

CONTEXTO

- El proyecto vive en /src, usa FastAPI, y no tiene base de datos real
  todavía: los datos se guardan en constantes de Python en memoria,
  dentro de src/data/mock_data.py.
- La lógica de cada recurso vive en un archivo de servicio dentro de
  src/services/, y las rutas se registran en src/main.py.
- Ya existe un recurso de ejemplo (health) siguiendo este patrón.
- Regla de negocio obligatoria: no se puede crear un pedido para una
  fecha si no existe una ruta con un camión ya asignado para ese día.
  Si no existe esa ruta, el pedido debe rechazarse.

ALCANCE

- Sí puedes: crear/editar archivos dentro de src/data/ y src/services/,
  y agregar las nuevas rutas a src/main.py.
- No toques: src/services/health_service.py, no agregues base de
  datos real, no agregues autenticación, no toques nada de frontend.

CRITERIOS DE ACEPTACIÓN (debe cumplir los 8, sin excepción)

1. La app arranca con uvicorn src.main:app --reload sin romper lo
   que ya existe.
2. Las rutas siguen convención REST en plural: /pedidos y
   /pedidos/{id}/estado.
3. Implementa la regla de negocio (rechaza el pedido si no hay ruta
   con camión asignado ese día), no solo el CRUD.
4. Valida la entrada (campos requeridos, formatos) y devuelve un error
   estructurado con el código HTTP correcto (400 para datos inválidos
   o regla de negocio violada, 404 si el pedido no existe).
5. Respeta la estructura de carpetas y el estilo de nombres ya usado
   en el proyecto (snake_case, data/ y services/ separados).
6. Devuelve el mismo estilo de respuesta que ya usa el recurso
   health: JSON plano, sin envoltorios adicionales.
7. Incluye al menos una prueba (pytest) que ejercite la regla de
   negocio con un caso que debe fallar, además del caso feliz.
8. Todas las dependencias que uses ya están en requirements.txt; si
   necesitas una nueva, decláramela explícitamente en vez de asumir
   que existe.

FORMATO DE SALIDA
Entrega los archivos completos (no diffs), indicando la ruta de cada
uno antes de su contenido. Al final, lista explícitamente cuál de los
8 criterios cumple cada archivo.

## Criterios de verificación

Criterio 1 - Arranque con un solo comando: No cumple

> Justificación: El comando uvicorn src.main:app --reload no aparece en README.md (solo "# README") ni en ningún otro archivo del repo; el arranque no está documentado y no hay evidencia en el repo de que se haya ejecutado con éxito.

Criterio 2 - Convención REST: Cumple

> Justificación: src/main.py líneas 51-68 expone POST /pedidos, GET /pedidos y PATCH /pedidos/{pedido_id}/estado, alineado con /pedidos y /pedidos/{id}/estado en plural.

Criterio 3 - Regla de negocio del RFP: Cumple

> Justificación: crear_pedido en src/services/pedido_service.py líneas 67-72 rechaza el alta si hay_ruta_con_camion_asignado es falso, usando mock_rutas; no es solo CRUD.

Criterio 4 - Validación de entrada y error estructurado: Cumple

> Justificación: PedidoCreate/EstadoUpdate validan campos y formato; main.py líneas 31-38 y 66-68 responden {"error": "..."} con 400 (datos o regla) y 404 (pedido inexistente).

Criterio 5 - Estructura de carpetas y nombres: Cumple

> Justificación: Sigue el patrón de health_service.py: datos en src/data/mock_data.py, lógica en src/services/pedido_service.py (snake_case), rutas en src/main.py; health_service.py no se modificó.

Criterio 6 - Formato de respuesta igual al de referencia: Cumple

> Justificación: health_service.py devuelve el dict plano de mock_health_data; POST/PATCH devuelven el dict del pedido y GET /pedidos una lista JSON, sin envoltorio tipo data/success.

Criterio 7 - Prueba de la regla de negocio: Cumple

> Justificación: tests/test_pedidos.py líneas 28-43 POST a fecha 2026-08-29 (ruta sin camión) espera 400 y que no crezca mock_pedidos; líneas 46-58 cubren el caso feliz.

Criterio 8 - Dependencias declaradas: Cumple

> Justificación: fastapi, uvicorn, pytest y httpx (TestClient) están en requirements.txt; pydantic se importa pero llega como dependencia de fastapi>=0.115, sin paquetes inventados fuera del manifiesto.

**Total cumplidos:** 7 de 8

## Alucinaciones

- mock_camiones (id, nombre "Truck A"/"Truck B") en src/data/mock_data.py líneas 7-10: no hay recurso ni requisito de catálogo de camiones; no lo usa ningún endpoint ni la regla de negocio.
- El chequeo exige ruta con el mismo camion_id del pedido (pedido_service.py líneas 50-58), no solo "una ruta con camión asignado ese día"; esa coincidencia camión-día no está en el enunciado V3 ni en el RFP citado.
- test_health_sigue_disponible en tests/test_pedidos.py: nadie pidió revalidar /health en la suite de pedidos.
- El cuerpo de error unificado {"error": "Datos inválidos"} en main.py línea 33 descarta el detalle de Pydantic; el recurso de referencia no define errores, pero este contrato de error no estaba pedido con esa forma fija.

## Conclusión

La V3 está funcionalmente lista en código (CRUD + regla + tests + manifiesto) y se cae el total solo por el criterio 1: el comando de arranque no está en el proyecto. Uno de los pocos fallos es que no esté documentado el comando de inicio del servidor en el README.md (uvicorn src.main:app --reload), porque al parecer la IA no entendió que podía modificar el README para documentar esto. Es necesario mejorar las alucinaciones que tuvo este prompt, aunque es una versión mucho más sólida en comparación de la versión 1 y 2.
Se abona, además, que hizo los tests unitarios, sin embargo fueron pocos tests y uno de ellos fue para el ejemplo de health, lo cual no era necesario y tampoco se le pedía que lo hiciera (se pedían tests para la regla de negocio).

# Prompt V4

## Prompt

Eres un desarrollador backend trabajando en el proyecto Food Truck Planner,
una API en FastAPI para Street Corner Eats (dos food trucks que reciben
pre-pedidos y necesitan coordinar rutas diarias).

OBJETIVO
Cuando termines debe existir en el backend:

1. Un endpoint para crear un pedido.
2. Un endpoint para listar pedidos, con filtro por estado, fecha y camión.
3. Un endpoint para cambiar el estado de un pedido (Received, Preparing,
   Ready, Picked Up).

CONTEXTO

- El proyecto vive en /src, usa FastAPI, y no tiene base de datos real
  todavía: los datos se guardan en constantes de Python en memoria,
  dentro de src/data/mock_data.py.
- La lógica de cada recurso vive en un archivo de servicio dentro de
  src/services/, y las rutas se registran en src/main.py.
- Regla de negocio obligatoria: no se puede crear un pedido para una
  fecha si no existe una ruta con un camión ya asignado para ese día.
  Si no existe esa ruta, el pedido debe rechazarse.

ALCANCE

- Sí puedes: crear/editar archivos dentro de src/data/ y src/services/,
  y agregar las nuevas rutas a src/main.py.
- No toques: src/services/health_service.py, no agregues base de
  datos real, no agregues autenticación, no toques nada de frontend.

CRITERIOS DE ACEPTACIÓN (debe cumplir los 8, sin excepción)

1. La app arranca con uvicorn src.main:app --reload sin romper lo
   que ya existe.
2. Las rutas siguen convención REST en plural: /pedidos y
   /pedidos/{id}/estado.
3. Implementa la regla de negocio (rechaza el pedido si no hay ruta
   con camión asignado ese día), no solo el CRUD.
4. Valida la entrada (campos requeridos, formatos) y devuelve un error
   estructurado con el código HTTP correcto (400 para datos inválidos
   o regla de negocio violada, 404 si el pedido no existe).
5. Respeta la estructura de carpetas y el estilo de nombres ya usado
   en el proyecto (snake_case, data/ y services/ separados).
6. Devuelve el mismo estilo de respuesta que ya usa el recurso
   health: JSON plano, sin envoltorios adicionales.
7. Incluye al menos una prueba (pytest) que ejercite la regla de
   negocio con un caso que debe fallar, además del caso feliz.
8. Todas las dependencias que uses ya están en requirements.txt; si
   necesitas una nueva, decláramela explícitamente en vez de asumir
   que existe.

FORMATO DE SALIDA
Entrega los archivos completos (no diffs), indicando la ruta de cada
uno antes de su contenido. Al final, lista explícitamente cuál de los
8 criterios cumple cada archivo.

EJEMPLOS DE CONVENCIÓN (sigue exactamente este mismo patrón)

### src/data/mock_data.py (existente)

mock_health_data = {
"status": "ok"
}

### src/services/health_service.py (existente)

from data.mock_data import mock_health_data

def get_health():
return mock_health_data

### src/main.py (existente, fragmento relevante de cómo se registran rutas)

from fastapi import FastAPI
from data.mock_data import mock_health_data
from services.health_service import get_health

app = FastAPI(
title="FastAPI Starter",
description="Baseline FastAPI project.",
version="0.1.0",
)

@app.get("/health")
def health():
return get_health()

## Criterios de verificación

1. Arranca con un solo comando y está documentado: No cumple
2. Uso de convención REST: Cumple
3. Implementa la regla de negocio del RFP: Cumple
4. Valida la entrada y devuelve errores estructurados: Cumple
5. Respeta estructura de carpetas y nombres de archivo: Cumple
6. Devuelve el mismo formato de respuesta que el archivo de referencia: Cumple
7. Incluye al menos una prueba que ejercita la regla de negocio: Cumple
8. Todas las dependencias existen y están declaradas: Cumple

**Total cumplidos:** 7 de 8

## Alucinaciones

No se observaron alucinaciones con este prompt. Todos los elementos generados son relevantes para la lógica de negocio y son usados en su totalidad.

## Conclusión

Con un prompt bien estructurado la IA creó el servicio con las operaciones necesarias para la lógica de negocio, las conectó adecuadamente con las rutas, los datos y los tests sin tocar nada de lo que ya existía. Se probó su funcionamiento: cuando intentamos crear un pedido para un día sin camión asignado lo rechazó con un mensaje claro, y cuando probamos un día válido lo creó sin problemas. Se ejecutaron las seis pruebas que escribió y todas funcionaron, cubriendo tanto el caso normal como dos formas distintas en las que la regla de negocio podía fallar, que es justo el tipo de detalle que suele pasarse por alto.
Adicionalmente, no se limitó al CRUD genérico: entendió que el objetivo era la regla del RFP y la puso en el centro, con un manejo de errores claro y uniforme en los tres endpoints.
