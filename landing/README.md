# Landing page: antes y después de la skill UI/UX Pro Max

Ejercicio del laboratorio de skills (Semana 13). Hicimos la misma landing dos veces con el mismo prompt:

> Crea una landing page para el Food Truck Planner de Street Corner Eats.

| Versión | Carpeta | Cómo se hizo |
|---|---|---|
| Sin skill | `sin_skill/index.html` | Prompt directo, sin guía de diseño |
| Con skill | `con_skill/index.html` | Skill [`ui-ux-pro-max`](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) (nextlevelbuilder, MIT), instalada en `.claude/skills/ui-ux-pro-max/` |

Para verlas basta con abrir cada `index.html` en el navegador. No usan dependencias ni red: las fuentes están en `fonts/` (SIL OFL, vía Fontsource) y los íconos son de Phosphor (MIT), embebidos como SVG. Las capturas de escritorio, página completa y móvil están en `capturas/`.

## Por qué esta skill

Primero probamos `frontend-design` (Anthropic), pero su resultado dependía del criterio estético del agente y no nos convenció. UI/UX Pro Max funciona distinto: busca en un catálogo local de estilos, paletas, tipografías y reglas de UX y devuelve un sistema de diseño concreto para el tipo de producto.

**Revisión de seguridad:** licencia MIT y sin caracteres invisibles. Su script `scripts/search.py` solo lee archivos CSV de `data/` y no hace llamadas de red. Instalamos solo la carpeta de la skill, sin sus pruebas internas.

## Cómo se usó la skill

**1. Análisis del pedido.**
- Producto: landing de un negocio de comida callejera.
- Público: clientes en el celular a la hora del almuerzo.
- Stack: HTML y CSS sin framework (no hay `package.json`), así que no se pidió guía de stack.

**2. Sistema de diseño.** Se generó con:

```bash
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "food truck street food restaurant landing" \
  --design-system --persist -p "Street Corner Eats" --output-dir .
```

El resultado quedó guardado en [`design-system/street-corner-eats/MASTER.md`](../design-system/street-corner-eats/MASTER.md):

| Decisión | Lo que propuso la skill |
|---|---|
| Patrón | Funnel de 3 pasos, con un color por paso (rojo, naranja, verde) |
| Estilo | Vibrant & Block-based: bloques de color, formas geométricas, tipografía grande |
| Paleta | Rojo apetitoso `#DC2626` y dorado cálido `#A16207`, fondo `#FEF2F2` y texto `#450A0A` |
| Tipografía | Playfair Display SC para títulos y Karla para el texto (pareja para restaurantes) |
| Efectos | Secciones con separación de 48px o más, patrón animado y transiciones de 200 a 300 ms |
| Evitar | Imágenes de baja calidad y horarios desactualizados |

**3. Búsquedas de apoyo.**
- `"inline validation error near field" --domain ux`: el error va debajo del campo, enlazado con `aria-describedby`.
- `"location hours map pin" --domain icons`: íconos Phosphor (`map-pin`, etc.) en lugar de emojis.

**4. Checklist de entrega de la skill.**
- Sin emojis como íconos.
- `cursor: pointer` en todo lo clicable.
- Hover de 200 ms.
- Contraste de texto de 4.5:1 o más.
- Foco visible.
- `prefers-reduced-motion` desactiva el patrón animado.
- Probado a 375, 768 y 1440 px sin scroll horizontal.

## Antes vs. después

| | Sin skill | Con UI/UX Pro Max |
|---|---|---|
| Estilo | Plantilla SaaS morada genérica | Sistema elegido para restaurantes: rojo y dorado, bloques de color |
| Hero | Eslogan "como un profesional" | Las paradas del día con horario, al lado del titular |
| Estructura | 6 tarjetas iguales con emoji | Funnel de 3 pasos, un color por paso, y los 4 estados del pedido |
| Íconos | Emojis | SVG de Phosphor con `aria-hidden` |
| Acción principal | "Empezar gratis →" (no aplica a un cliente) | "Consultar mi pedido", con una consulta que funciona |
| Errores | No hay formulario | Error junto al campo, con `aria-invalid` y `aria-describedby` |
| Promesas | "Seguimiento en tiempo real" (fuera del MVP) | Solo lo que el MVP incluye |

Ajustes tras revisar las capturas:
- En los títulos, la tipografía unía "fi" en una ligadura minúscula. Se desactivaron las ligaduras.
- En móvil el logo partía en dos líneas. Se redujo su tamaño.

## Notas

- Las paradas y horarios son contenido de ejemplo. En la app real saldrían de las rutas del día.
- La consulta usa datos de ejemplo con la forma de `GET /pedidos`. La API todavía no tiene un endpoint para consultar un pedido por número; sería una feature para especificar con OpenSpec.
- `AGENTS.md` restringe modificar el frontend en las tareas de backend. Esta landing es un entregable aparte del laboratorio y no toca `src/`.
