# Landing page: antes y después de la skill `frontend-design`

Ejercicio del laboratorio de skills (Semana 13). Hicimos la misma landing dos veces con el mismo prompt:

> Crea una landing page para el Food Truck Planner de Street Corner Eats.

| Versión | Carpeta | Cómo se hizo |
|---|---|---|
| Sin skill | `sin_skill/index.html` | Prompt directo, sin guía de diseño |
| Con skill | `con_skill/index.html` | Skill [`frontend-design`](https://github.com/anthropics/skills/tree/main/skills/frontend-design) (Anthropic, Apache 2.0) |

Para verlas basta con abrir cada `index.html` en el navegador. No usan dependencias ni red: las fuentes están en `fonts/` (licencia SIL OFL, vía Fontsource). Las capturas de escritorio, página completa y móvil están en `capturas/`.

## Qué hizo la skill distinto

La skill pide trabajar en dos pasadas: primero un plan de diseño, revisarlo contra lo genérico y solo después escribir código, criticando con capturas.

### 1. Sujeto y trabajo de la página

La versión sin skill vendió "la plataforma" con frases genéricas. La skill obliga a definir antes para quién es la página:

- **Quién la usa:** clientes de Street Corner Eats, desde el celular a la hora del almuerzo.
- **Qué necesitan:** saber dónde está cada camión hoy y si su pedido ya está listo.
- **De dónde sale el contenido:** del alcance del MVP: vista de la agenda diaria de los camiones, los estados del pedido y la consulta opcional del cliente.

### 2. Plan de diseño

**Color**
- Asfalto `#22302F`: la calle.
- Pintura de andén `#F2C230`: la franja amarilla y el paso "Listo para recoger".
- Teal `#0E6E66`: las placas de cada parada (el color de la marca en los mockups).
- Cielo `#EEF3F2`: el fondo de lectura, frío en vez de crema.
- Tinta `#142624`: el texto.

**Tipografía**
- Big Shoulders Display (800/900): titulares y nombres de esquinas, como la señalización urbana.
- Atkinson Hyperlegible (400/700): el resto, legible en un celular bajo el sol.

**Layout**

```
[Street Corner Eats]                         [Consulta tu pedido]
Jueves 28 de agosto
HOY ESTAMOS EN DOS ESQUINAS.            (titular gigante)
┌ Camión 1 ───────────────┐ ┌ Camión 2 ───────────────┐
│ Calle 10 con Carrera 43 │ │ Parque de los Deseos    │  ← placas de calle
│ 11:30 a. m. a 3:00 p. m.│ │ 12:00 m. a 4:00 p. m.   │
└─────────────────────────┘ └─────────────────────────┘
▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ (franja de andén) ▀▀▀ ▀▀▀ ▀▀▀
Así avanza tu pedido  1 Recibido · 2 En preparación · 3 Listo · 4 Entregado
[ Consulta tu pedido:  ( número ) [Consultar estado]  → resultado ]
```

Todo alineado a la izquierda. Los pasos van numerados porque sí son una secuencia.

**Principios**
1. Lo primero que se ve es la información del día, no un eslogan.
2. Una sola pieza llamativa: las placas de parada sobre el asfalto. Lo demás es sobrio.
3. Cada texto hace un trabajo: el botón dice "Consultar estado" y los errores dicen cómo arreglarlo.
4. La consulta es pública, así que solo muestra el primer nombre del cliente.

### 3. Revisión contra lo genérico (antes de programar)

La versión sin skill cayó en casi todos los patrones que la skill marca como genéricos. Los quitamos en la versión con skill:

| Patrón genérico (sin skill) | Decisión con skill |
|---|---|
| Hero centrado con degradado y una frase resaltada en otro color | Hero con las paradas reales del día |
| Etiqueta en mayúsculas sobre cada título ("FUNCIONALIDADES") | Sin etiquetas: el título ya dice qué es |
| Seis tarjetas iguales con emoji y sombra gris | Una secuencia de 4 pasos y una herramienta de consulta |
| Números grandes de relleno ("100% en la nube") | Ninguna estadística que el cliente no necesite |
| Botones con flecha "Comienza ahora →" y "Empezar gratis" | Una acción concreta: "Consultar estado" |
| Promete "seguimiento en tiempo real", que está fuera del MVP | Solo lo que el MVP incluye |

### 4. Crítica con capturas

- En móvil, el nombre de la marca partía en dos líneas la barra superior. Se redujo el tamaño en pantallas angostas.
- La consulta se probó con un pedido existente (`4`), uno inexistente (`99`) y un texto inválido (`abc`). Cada caso muestra un mensaje distinto y útil.

## Notas

- Las paradas y horarios son contenido de ejemplo. En la app real saldrían de las rutas del día.
- La consulta usa datos de ejemplo con la forma de `GET /pedidos`. Hoy la API no tiene un endpoint para consultar un pedido por número; sería una feature por especificar con OpenSpec.
- `AGENTS.md` restringe modificar el frontend en las tareas de backend. Esta landing es un entregable aparte del laboratorio y no toca `src/`.
