# Plantilla: Prompt para generación de tests

## 1. Objetivo

Generar los tests automatizados para `[funcionalidad / endpoint / servicio / componente]` ubicado en `[ruta del archivo o módulo]`.

Al terminar debe existir una suite de tests que verifique de forma automatizada el comportamiento esperado de `[funcionalidad]`, incluyendo los casos exitosos, errores, validaciones y casos límite relevantes.

Los tests deben detectar regresiones reales en la implementación y deben ejecutarse correctamente utilizando `[framework de testing]`.

## 2. Contexto

- **Stack:** [framework, lenguaje, versión — ej. Laravel 11 / PHP 8.3, Django 5 / Python 3.12]
- **Framework de tests:** [ej. PHPUnit, Pest, Pytest, Jest, Vitest]
- **Tipo de tests:** [unitarios / integración / feature / API / E2E]
- **Ubicación de la implementación que se debe probar:**
  - Endpoint/controlador: `[ruta]`
  - Servicio/caso de uso: `[ruta, si aplica]`
  - Modelo(s): `[ruta, si aplica]`
  - Validación: `[ruta, si aplica]`
- **Ubicación de los tests existentes:** `[ruta]`
- **Base de datos / ORM:** [ej. PostgreSQL + Django ORM]
- **Autenticación / autorización:** [cómo se autentica el usuario y qué roles/permisos existen]
- **Dependencias externas:** [APIs, servicios, colas, almacenamiento, etc.]
- **Fixtures / factories / mocks existentes:** [rutas o ejemplos relevantes]
- **Configuración relevante para tests:** [variables, base de datos de test, configuración especial, etc.]
- **Convenciones del proyecto:** [naming, estructura de tests, patrón AAA, Given/When/Then, uso de factories, mocks, fixtures, etc.]

**Importante:** antes de generar los tests, inspecciona la implementación que se está probando y los tests existentes relacionados. No inventes comportamiento que no esté definido por el código, los requisitos o los ejemplos proporcionados.

## 3. Alcance

### Sí tocar / sí crear

- Crear o modificar `[ruta del archivo de test]`.
- Crear los fixtures/factories/helpers necesarios solo si ya existe ese patrón en el proyecto.
- Añadir los tests necesarios para cubrir los criterios de aceptación definidos en este prompt.
- `[Otro archivo de test permitido, si aplica]`.

### NO tocar bajo ninguna circunstancia

- La implementación de `[endpoint / servicio / componente]` para hacer que los tests pasen.
- Otros endpoints, servicios o módulos que no estén directamente relacionados.
- Migraciones existentes.
- Configuración global del proyecto.
- Dependencias del proyecto.
- Tests existentes que no estén directamente relacionados.
- `[Otra restricción específica del proyecto]`.

### Fuera de alcance para este prompt

- Tests de carga o performance.
- Tests E2E, si este prompt genera únicamente tests de integración/API.
- Modificar la lógica de negocio.
- Refactorizar código de producción.
- Añadir nuevas librerías de testing.
- Corregir bugs descubiertos durante la generación de tests.

**Regla importante:** si un test falla debido a un comportamiento incorrecto de la implementación, **no modifiques el código de producción para que el test pase**. Reporta el fallo y explica qué comportamiento está causando el problema.

## 4. Criterios de aceptación

### Cobertura funcional

- [ ] Existe al menos un test para el caso exitoso.
- [ ] Existe un test para cada condición de error definida: `[listar errores]`.
- [ ] Se prueban todas las validaciones relevantes: `[listar campos/reglas]`.
- [ ] Se prueba el comportamiento cuando `[recurso relacionado]` no existe.
- [ ] Se prueba el comportamiento cuando `[recurso relacionado]` ya existe / está duplicado, si aplica.
- [ ] Se prueba la autorización para cada rol/permisión relevante.
- [ ] Se prueba el comportamiento de un usuario no autenticado, si aplica.
- [ ] Se prueban los casos límite relevantes: `[listar casos límite]`.
- [ ] Se verifica el código HTTP / resultado esperado en cada escenario.
- [ ] Se verifica la estructura y contenido relevante de la respuesta.
- [ ] Se verifica el estado de la base de datos después de operaciones que modifican datos.
- [ ] Se verifica que no se creen/modifiquen datos cuando la operación debe fallar.
- [ ] Las dependencias externas se mockean/stubbean siguiendo las convenciones existentes del proyecto.
- [ ] Los tests son independientes entre sí y no dependen del orden de ejecución.
- [ ] Los tests existentes siguen pasando.

### Calidad de los tests

- [ ] Cada test verifica un comportamiento concreto.
- [ ] Los nombres de los tests describen claramente el comportamiento esperado.
- [ ] Los tests siguen la estructura y convenciones de los tests existentes.
- [ ] No se hacen assertions innecesarias sobre detalles de implementación que no formen parte del contrato.
- [ ] No se duplican fixtures/helpers existentes sin necesidad.
- [ ] Los tests no dependen de datos externos ni de servicios reales.
- [ ] No se modifica código de producción para conseguir que los tests pasen.
- [ ] La suite generada puede ejecutarse con `[comando para ejecutar los tests]`.

### Escenarios concretos

La IA debe cubrir como mínimo los siguientes escenarios:

| Escenario           | Entrada / condición | Resultado esperado     |
| ------------------- | ------------------- | ---------------------- |
| Caso exitoso        | `[datos]`           | `[resultado]`          |
| `[Error 1]`         | `[condición]`       | `[resultado esperado]` |
| `[Error 2]`         | `[condición]`       | `[resultado esperado]` |
| No autenticado      | `[condición]`       | `[resultado]`          |
| Sin permisos        | `[condición]`       | `[resultado]`          |
| Recurso inexistente | `[condición]`       | `[resultado]`          |
| Caso límite         | `[condición]`       | `[resultado]`          |

## 5. Formato de salida

- **Tipo de entrega:** [diff / archivos completos / solo tests nuevos].
- **Archivos que puede crear/modificar:** `[listar rutas]`.
- **Explicación:** [ninguna / breve explicación después del código].
- **Framework:** `[PHPUnit / Pest / Pytest / Jest / etc.]`.
- **Comando de ejecución:** `[comando]`.
- **Comentarios en el código:** [no incluir / inglés / español].
- **Si detectas un comportamiento ambiguo:** no inventarlo; indícalo al final de la respuesta.
- **Si detectas un bug en producción:** no modificarlo; indicar qué test lo detecta y por qué falla.

La respuesta debe estar organizada de la siguiente manera:

1. Archivos creados/modificados.
2. Código de los tests.
3. Breve explicación de los escenarios cubiertos.
4. Ambigüedades, supuestos o problemas encontrados, si existen.

## 6. Ejemplos

### Ejemplo de test existente con el mismo patrón

Usa este test como referencia para estructura, naming, setup, assertions, factories, mocks y organización:

[pegar aquí un test existente similar]

### Ejemplo de test existente con el mismo patrón

[pegar aquí el endpoint / servicio / componente]

### Ejemplo de factory / fixture

[pegar aquí una factory o fixture existente]

### Ejemplo de comportamiento esperado

**Request:**
{
"campo1": "valor",
"campo2": 123
}
**Response esperada:**
{
"status": "success",
"data": {}
}
**Caso de error:**
{
"status": "error",
"message": "..."
}
