# Plantilla: Prompt para generación de documentación de proyecto

## 1. Objetivo

Generar la documentación de `[proyecto / módulo / funcionalidad / endpoint / servicio]` a partir del código y de la información proporcionada.

Al terminar debe existir una documentación clara, completa y actualizada que permita a `[desarrolladores / QA / DevOps / usuarios técnicos / nuevos miembros del equipo]` entender `[qué debe poder hacer el lector con esta documentación]`.

La documentación debe reflejar el comportamiento real de la implementación actual.

El objetivo principal de esta documentación es:

- [ ] Explicar la arquitectura o estructura del proyecto.
- [ ] Explicar cómo instalar y ejecutar el proyecto.
- [ ] Explicar cómo utilizar `[módulo / API / funcionalidad]`.
- [ ] Documentar endpoints y contratos de API.
- [ ] Documentar configuración y variables de entorno.
- [ ] Documentar modelos y relaciones.
- [ ] Documentar procesos o flujos de negocio.
- [ ] Facilitar el onboarding de nuevos desarrolladores.
- [ ] Documentar procedimientos de desarrollo, testing o despliegue.
- [ ] Otro: `[especificar]`.

## 2. Contexto

- **Proyecto:** `[nombre del proyecto]`
- **Descripción:** `[descripción breve del proyecto]`
- **Stack:** [framework, lenguaje, versiones — ej. Laravel 11 / PHP 8.3, Django 5 / Python 3.12]
- **Arquitectura:** [monolito / microservicios / serverless / MVC / Clean Architecture / etc.]
- **Base de datos / ORM:** `[tecnología]`
- **Frontend:** `[tecnología, si aplica]`
- **Backend:** `[tecnología]`
- **API:** `[REST / GraphQL / gRPC / etc.]`
- **Autenticación / autorización:** `[JWT / OAuth / sesiones / roles / permisos / etc.]`
- **Servicios externos:** `[APIs, proveedores, colas, almacenamiento, etc.]`
- **Infraestructura / despliegue:** `[Docker / Kubernetes / AWS / Azure / etc.]`
- **Repositorio / estructura del proyecto:** `[ruta o descripción]`
- **Documentación existente:** `[rutas de README, docs, ADRs, OpenAPI, etc.]`
- **Configuración relevante:** `[archivos .env.example, config, etc.]`

### Fuentes de información

La documentación debe generarse utilizando, en orden de prioridad:

1. Código fuente actual.
2. Tests existentes.
3. Configuración del proyecto.
4. Contratos/API schemas existentes.
5. Documentación existente.
6. Requisitos proporcionados explícitamente en este prompt.

Si existe una contradicción entre la documentación existente y el código actual, considera el código como fuente de verdad y señala la discrepancia.

**No inventes información que no pueda ser verificada en el código, configuración, tests o requisitos proporcionados.**

Si una información no puede determinarse, indícalo explícitamente como `[NO DOCUMENTADO]` o `[REQUIERE CONFIRMACIÓN]`.

## 3. Alcance

### Sí tocar / sí crear

- Crear o actualizar `[ruta del archivo de documentación]`.
- Documentar `[módulo / funcionalidad / componente]`.
- Actualizar el README si forma parte del alcance: `[sí/no]`.
- Crear documentación adicional en `[ruta]` si es necesario.
- Documentar ejemplos de uso cuando puedan deducirse de forma fiable de la implementación.
- Documentar los endpoints, parámetros, respuestas y errores definidos actualmente.
- Documentar las configuraciones necesarias para ejecutar `[funcionalidad/proyecto]`.

### NO tocar bajo ninguna circunstancia

- Código de producción.
- Tests existentes.
- Migraciones.
- Configuración del proyecto.
- Dependencias.
- Contratos de API.
- Código generado automáticamente.
- Documentación fuera del alcance indicado.
- `[otra restricción específica]`.

La tarea es exclusivamente de **documentación**.

**No modifiques el código para adaptarlo a la documentación.**

Si encuentras un problema, inconsistencia o comportamiento inesperado en el código, documenta el problema pero no lo corrijas.

### Fuera de alcance para este prompt

- Refactorizar código.
- Corregir bugs.
- Implementar funcionalidades.
- Crear nuevos endpoints.
- Crear o modificar tests.
- Cambiar arquitectura.
- Cambiar dependencias.
- Modificar infraestructura.
- Crear funcionalidades que únicamente aparezcan descritas en documentación pero que no existan en el código actual.

## 4. Criterios de aceptación

### Exactitud

- [ ] La documentación refleja el comportamiento actual de la implementación.
- [ ] No se inventan funcionalidades, endpoints, parámetros, configuraciones o comportamientos.
- [ ] Los nombres de clases, funciones, endpoints, modelos y archivos coinciden con los existentes en el proyecto.
- [ ] Las rutas de archivos documentadas existen realmente.
- [ ] Los ejemplos proporcionados son compatibles con la implementación actual.
- [ ] Los códigos HTTP, formatos de respuesta y mensajes documentados coinciden con la implementación cuando sean verificables.
- [ ] Las variables de entorno documentadas existen realmente o están explícitamente marcadas como requeridas/no verificadas.
- [ ] Las relaciones entre entidades documentadas coinciden con los modelos y migraciones existentes.

### Completitud

La documentación debe cubrir, cuando aplique:

- [ ] Descripción general del proyecto.
- [ ] Requisitos previos.
- [ ] Instalación.
- [ ] Configuración.
- [ ] Variables de entorno.
- [ ] Ejecución local.
- [ ] Estructura del proyecto.
- [ ] Arquitectura.
- [ ] Principales módulos y responsabilidades.
- [ ] Modelos y relaciones.
- [ ] Endpoints/API.
- [ ] Autenticación y autorización.
- [ ] Validaciones.
- [ ] Manejo de errores.
- [ ] Dependencias externas.
- [ ] Jobs, colas o procesos asíncronos.
- [ ] Testing.
- [ ] Build.
- [ ] Despliegue.
- [ ] Logs y observabilidad.
- [ ] Consideraciones conocidas o limitaciones.

Solo incluir las secciones que sean relevantes para el proyecto.

### API / endpoints

Si se documentan endpoints, cada uno debe incluir cuando aplique:

- [ ] Método HTTP.
- [ ] URL/path.
- [ ] Autenticación requerida.
- [ ] Roles/permisos requeridos.
- [ ] Parámetros de path.
- [ ] Query parameters.
- [ ] Headers relevantes.
- [ ] Body/request.
- [ ] Campos requeridos y opcionales.
- [ ] Reglas de validación.
- [ ] Ejemplo de request.
- [ ] Respuesta exitosa.
- [ ] Códigos HTTP.
- [ ] Respuestas de error.
- [ ] Ejemplos de errores.

### Calidad

- [ ] La documentación utiliza una estructura consistente.
- [ ] Utiliza Markdown siguiendo las convenciones existentes del proyecto.
- [ ] Los términos técnicos se utilizan consistentemente.
- [ ] Los ejemplos son claros y realistas.
- [ ] No se documentan detalles de implementación innecesarios cuando no aporten valor al lector.
- [ ] No se incluyen secretos, contraseñas, tokens, API keys ni información sensible.
- [ ] No se incluyen grandes bloques de código cuando una explicación o referencia sea suficiente.
- [ ] Los enlaces internos apuntan a archivos o secciones existentes.
- [ ] No se duplican innecesariamente contenidos que ya estén documentados en otra ubicación.

### Consistencia

- [ ] La nueva documentación sigue el estilo de la documentación existente.
- [ ] La estructura sigue los ejemplos proporcionados.
- [ ] La terminología coincide con la utilizada en el código.
- [ ] Los nombres de módulos, entidades y componentes son consistentes en todo el documento.
- [ ] No existen contradicciones internas en la documentación.

### Validación final

Antes de entregar la documentación:

- [ ] Revisar el código relevante.
- [ ] Revisar los tests relacionados.
- [ ] Revisar la documentación existente.
- [ ] Comprobar que los archivos referenciados existen.
- [ ] Comprobar que los comandos documentados son coherentes con la configuración del proyecto.
- [ ] Comprobar que los ejemplos coinciden con el comportamiento actual.
- [ ] Identificar cualquier información que no haya podido verificarse.

## 5. Formato de salida

- **Tipo de entrega:** [archivo completo / diff / contenido Markdown].
- **Archivo(s) a crear/modificar:** `[rutas]`.
- **Formato:** Markdown.
- **Idioma:** [español / inglés].
- **Nivel de detalle:** [breve / medio / exhaustivo].
- **Audiencia:** [desarrolladores / QA / DevOps / usuarios técnicos / público general].
- **Explicación adicional:** [ninguna / breve resumen / detallada].

La respuesta debe estar organizada de la siguiente manera:

1. Archivos creados o modificados.
2. Documentación generada.
3. Breve resumen de lo documentado.
4. Información que no pudo verificarse.
5. Inconsistencias o problemas encontrados, si existen.

**No incluyas explicaciones sobre código que no puedan verificarse en el proyecto.**

Si detectas una discrepancia entre documentación existente y código, no la ocultes. Indícala explícitamente.

## 6. Ejemplos

### Ejemplo de documentación existente

Usa este documento como referencia para estructura, estilo, nivel de detalle, terminología y formato:

[pegar aquí un README, documento técnico o sección de documentación existente]

### Ejemplo de documentación de un módulo similar

Usa este documento como referencia para documentar funcionalidades similares:

[pegar aquí documentación existente de un módulo similar]

### Ejemplo de código fuente relacionado

Este es un ejemplo del código que debe utilizarse como fuente de verdad para la documentación:

[pegar aquí el código fuente relevante]

### Ejemplo de endpoint documentado

Usa este ejemplo como referencia para documentar endpoints:

### POST /api/orders

Crea un nuevo pedido.

**Autenticación:** Bearer Token

**Permisos:** `orders.create`

#### Request

    {
      "customer_id": 123,
      "product_id": 456,
      "quantity": 2
    }

#### Response — 201 Created

    {
      "status": "success",
      "data": {
        "id": 789
      }
    }

#### Response — 422 Unprocessable Entity

    {
      "status": "error",
      "message": "The quantity field is required."
    }

### Ejemplo de estructura esperada

La documentación final debe seguir, cuando sea aplicable, una estructura similar a:

# Nombre del proyecto

## Descripción

[Descripción general del proyecto]

## Requisitos

[Requisitos necesarios para ejecutar el proyecto]

## Instalación

[Pasos de instalación]

## Configuración

[Configuración y variables de entorno]

## Estructura del proyecto

[Descripción de las principales carpetas y módulos]

## Arquitectura

[Descripción de la arquitectura y principales componentes]

## API

[Documentación de endpoints]

## Autenticación y autorización

[Descripción del sistema de autenticación y permisos]

## Testing

[Cómo ejecutar los tests]

## Despliegue

[Proceso de despliegue]

## Limitaciones y consideraciones

[Limitaciones conocidas o aspectos importantes]
