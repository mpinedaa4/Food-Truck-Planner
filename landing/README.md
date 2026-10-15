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

## Versión final: `final/index.html`

La mejor versión combina dos skills, cada una para lo que hace mejor:

| Skill | Para qué se usó |
|---|---|
| `ui-ux-pro-max` | Patrón de página (`restaurant food ordering` → Hero-Centric + Conversion), paleta y tipografía del `MASTER.md`, override de página en `design-system/street-corner-eats/pages/landing.md` (máximo 1–2 elementos animados por vista, respetar movimiento reducido) y reglas de UX: indicador de progreso, feedback al enviar, teclado numérico, error junto al campo, CTA fija en móvil |
| `frontend-design` | La pieza memorable (ilustración SVG propia del camión llegando a la esquina), revisión contra lo genérico (se quitó la palabra resaltada en otro color del titular), copy desde el lado del cliente y crítica con capturas |

Qué tiene de nuevo frente a `con_skill`:
- Hero con una ilustración original del camión en la Calle 10, que entra rodando una sola vez al cargar (estática con movimiento reducido).
- Paradas del día sobre una franja de asfalto, con el estado "Abierto hoy".
- Sección "En la plancha hoy" con los productos que ya existen en los datos de ejemplo de la API. Sin precios inventados.
- Consulta de pedido con estado de carga y una barra de progreso de 4 pasos que marca en qué va el pedido.
- Navegación fija con enlaces a cada sección y, en móvil, un botón fijo "Consultar mi pedido" al alcance del pulgar.

Crítica con capturas (una pasada):
- El letrero del camión se salía del tablero amarillo; se ajustó el texto al ancho.
- Los botones del hero tocaban la franja de asfalto; se agregó espacio.

Verificado: sin scroll horizontal a 375, 768, 1024 y 1440 px; consulta probada con `4` (listo), `99` (no existe), `abc` y campo vacío.

## Notas

- Las paradas y horarios son contenido de ejemplo. En la app real saldrían de las rutas del día.
- La consulta usa datos de ejemplo con la forma de `GET /pedidos`. La API todavía no tiene un endpoint para consultar un pedido por número; sería una feature para especificar con OpenSpec.
- `AGENTS.md` restringe modificar el frontend en las tareas de backend. Esta landing es un entregable aparte del laboratorio y no toca `src/`.
