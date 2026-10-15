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

La versión final usa seis skills. Cada una se revisó antes de usarla, con la misma plantilla del catálogo.

| Skill | Fuente y licencia | Para qué se usó |
|---|---|---|
| `ui-ux-pro-max` | nextlevelbuilder, MIT | Marca: paleta roja y tipografía Playfair Display SC + Karla del `MASTER.md`; override `pages/landing.md`; reglas de UX (progreso, carga, teclado numérico, error junto al campo) |
| `design-taste-frontend` (taste-skill) | Leonxlnx, MIT | Dirección de arte con `draw.mjs` (sector restaurante, semilla 1346289235): **"The name as a monument"**, con el nombre partido a dos esquinas. House rules, `lint.mjs` y el inspector en navegador real (`inspect.mjs`) a 1440, 768 y 390 px |
| `frontend-design` | Anthropic, Apache 2.0 | La idea desde el sujeto, el copy y la crítica con capturas |
| `web-design-guidelines` | Vercel, MIT | Auditoría contra las Web Interface Guidelines, leídas de una copia fijada (commit `434b7f9`) en vez de descargarlas en cada uso |
| `accessibility-audit` (AccessLint) | AccessLint, MIT | Método WCAG 2.2 AA. El motor se cambió por `axe-core@4.10.2` fijado, porque la skill instala `@latest` sin versión |
| `webapp-testing` | Anthropic, Apache 2.0 | `verificar_landing.py`: 23 pruebas de interacción con Playwright |

**La idea.** El nombre del cliente es "Street Corner Eats" y su condición es que cambia de esquina cada día. En la página, la esquina donde para el camión se vuelve el nombre partido a dos esquinas de la pantalla: "Street Corner" arriba a la izquierda y "Eats" abajo a la derecha, fijos mientras pasan las paradas del día.

**Lo vivo.** Eliges Camión 1 o 2 y el letrero de calle cambia de esquina. La página calcula con la hora real de Medellín si está abierto, cuánto falta para que cierre o a qué hora abre. Hay enlace directo con `#camion-2`.

**Secciones**, según la dirección de taste-skill:
1. El nombre partido con el letrero de calle.
2. Las dos esquinas de hoy.
3. El menú como tabla en una sola talla, con los productos de los datos de ejemplo y sin precios inventados.
4. Un acordeón de paneles en tonos de rojo, de oscuro a claro, con los 4 estados del pedido.
5. La consulta de pedido con barra de progreso.
6. Una banda roja donde toda la palabra "Ubícanos" es el botón.
7. El pie, que abre con el nombre.

### Resultados de las verificaciones

| Verificación | Resultado |
|---|---|
| taste-skill `lint.mjs` | 0 fallas. 2 avisos por usar Playfair Display: se mantiene porque es la tipografía de marca de `ui-ux-pro-max` (`--keep palette,type`) |
| taste-skill `inspect.mjs` | 1 falla y 1 aviso, explicados abajo. Ningún titular pasa de dos líneas, no hay texto tapado, no hay etiquetas sobre los títulos, 5 tallas de letra |
| axe-core (WCAG 2.2 AA + buenas prácticas) | 0 violaciones a 1440 y 390 px. El contraste más bajo es 4.41:1, de "Eats" en rojo sobre el fondo, que a 216px cumple el mínimo de 3:1 para texto grande |
| Web Interface Guidelines (Vercel) | Corregido: animación de layout en el acordeón, hover en sus botones y enlace directo al camión elegido |
| `verificar_landing.py` (webapp-testing) | 23 de 23. Sin scroll horizontal a 1440, 1024, 768 y 390 px; selector con mouse, flechas y `#camion-2`; acordeón; consulta con 4, 2, 99, `abc` y vacío; movimiento reducido |

**Pendiente: fotos.** El inspector de taste-skill exige al menos 4 fotografías reales y sugiere un video. Su script `assets.mjs` las busca en Openverse, Wikimedia Commons y museos, pero la red de este entorno solo permite registros de paquetes. Por eso la página solo tiene dibujos SVG, que no cuentan. Con fotos reales de los camiones o de las esquinas, el siguiente paso es ponerlas en las paradas y en el pie.

Ajustes que salieron de las capturas:
- El nombre fijo invadía el menú al terminar su recorrido; se limitó a las dos primeras pantallas.
- En el acordeón, los títulos de los paneles cerrados se desbordaban; ahora van en vertical.
- En móvil, "Eats" tapaba el horario; ahora el nombre va en dos líneas sobre el contenido.
- "Ubícanos" se cortaba en el borde derecho; se ajustó su tamaño.

`final/index_v1.html` ya no existe: la primera versión final queda en el historial del PR #14.

## Notas

- Las paradas y horarios son contenido de ejemplo. En la app real saldrían de las rutas del día.
- La consulta usa datos de ejemplo con la forma de `GET /pedidos`. La API todavía no tiene un endpoint para consultar un pedido por número; sería una feature para especificar con OpenSpec.
- `AGENTS.md` restringe modificar el frontend en las tareas de backend. Esta landing es un entregable aparte del laboratorio y no toca `src/`.
