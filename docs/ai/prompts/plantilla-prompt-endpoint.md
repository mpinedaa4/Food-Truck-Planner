# Plantilla: Prompt para endpoint de backend

## 1. Objetivo

Implementar el endpoint `[MÉTODO] /ruta/del/endpoint` que [qué hace, en una frase].

Al terminar debe poder: [acción concreta que un humano puede probar].

## 2. Contexto

- **Stack:** [framework, lenguaje, versión — ej. Laravel 11 / PHP 8.3, Django 5 / Python 3.12]
- **Base de datos / ORM:** [ej. MySQL + Eloquent, PostgreSQL + Django ORM]
- **Ubicación del código:**
  - Rutas: `[ruta al archivo de rutas]`
  - Controlador/vista: `[ruta]`
  - Modelo(s) involucrados: `[ruta]`
  - Validación: `[ruta, si está separada del controlador]`
- **Entidades del modelo de datos que participan:** [ej. `Pedido`, `DetallePedido`, `Producto` — referenciar el ERD si aplica]
- **Autenticación / roles:** [qué guard, middleware o rol puede pegarle a este endpoint — ej. "solo `Owner/Dispatcher`, vía middleware `role:dispatcher`"]
- **Dependencias externas:** [otro servicio, librería, o endpoint del que depende]
- **Convenciones del proyecto:** [naming, estructura de carpetas, patrón usado — Repository, Service Layer, etc., si el proyecto ya tiene uno]

## 3. Alcance

**Sí tocar / sí crear:**

- [archivo o capa 1]
- [archivo o capa 2]

**NO tocar bajo ninguna circunstancia:**

- [ej. migraciones ya aplicadas en producción]
- [ej. otros endpoints o módulos]
- [ej. el esquema de la base de datos — si necesita cambiar, es un prompt aparte]
- [ej. no instalar librerías nuevas sin preguntar]

**Fuera de alcance para este prompt (aunque esté relacionado):**

- [ej. el frontend que consume este endpoint]
- [ej. tests de carga / performance]

## 4. Criterios de aceptación

- [ ] El endpoint responde `[status code]` en el caso exitoso con [forma del body de respuesta].
- [ ] Devuelve `[status code]` si [condición de error 1, ej. faltan campos requeridos], con mensaje `[formato del error]`.
- [ ] Devuelve `[status code]` si [condición de error 2, ej. usuario sin el rol correcto].
- [ ] Valida: [lista de reglas de validación por campo — tipo, requerido, formato, longitud].
- [ ] Persiste correctamente en `[tabla(s)]`, respetando las relaciones [ej. `Pedido` → `DetallePedido`].
- [ ] No permite [acción que debe estar explícitamente bloqueada, ej. crear un pedido con `producto_id` inexistente].
- [ ] Incluye [autenticación / autorización] antes de ejecutar la lógica.
- [ ] Pasa las pruebas [manuales / automatizadas] descritas abajo.
- [ ] No rompe ningún endpoint o test existente.

## 5. Formato de salida

- **Tipo de entrega:** [diff / archivo(s) completo(s) / solo el bloque de código nuevo]
- **Explicación:** [sí, breve, al final / no, solo código / sí, línea por línea]
- **Migraciones:** [incluir archivo de migración si aplica sí/no]
- **Tests:** [incluir tests automatizados sí/no, y con qué framework — ej. PHPUnit, Pytest]
- **Idioma de comentarios/commits:** [español / inglés]

## 6. Ejemplos

**Ejemplo de endpoint ya existente con el mismo patrón a seguir:**

```
[pegar aquí el controlador/vista de un endpoint similar ya implementado]
```

**Ejemplo de request esperado:**

```json
{
  "campo1": "valor",
  "campo2": 123
}
```

**Ejemplo de response esperado (caso exitoso):**

```json
{
  "status": "success",
  "data": {}
}
```

**Ejemplo de response esperado (caso de error):**

```json
{
  "status": "error",
  "message": ""
}
```
