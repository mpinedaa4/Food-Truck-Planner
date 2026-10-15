# Demo UX/UI: antes y después de `frontend-design`

Prompt igual para ambas versiones: *"Crea la pantalla de pedidos del día para el dispatcher del Food Truck Planner"*, con los mismos datos (forma de `GET /pedidos`).

- `antes.html`: generada sin la skill.
- `despues.html`: generada con la skill [`frontend-design`](https://github.com/anthropics/skills/tree/main/skills/frontend-design) (Anthropic, Apache 2.0), siguiendo su proceso: plan, revisión contra el brief, construcción y crítica con capturas.

## Plan de diseño (paso 1 de la skill)

**Sujeto.** El dispatcher de Street Corner Eats revisa en una tablet, en la cocina central, qué pedidos esperan a su cliente y en qué camión. El trabajo principal de la pantalla: ver de un vistazo qué está listo y mover cada pedido al siguiente estado.

**Color**
- Riel `#23393B`: la barra de acero de donde cuelgan las comandas.
- Espacio de trabajo `#D9E4E1`: gris verdoso frío, no crema.
- Comanda `#FFFDF8`: papel térmico.
- Tinta `#15292B`: texto.
- Teal `#0E6E66`: acciones y Camión 1 (color de la marca en los mockups).
- Ámbar `#F2A93B`: solo para "Listo para recoger", lo único que debe gritar.

**Tipografía**
- Barlow Condensed (600/700): números de pedido, carriles y título, como los tableros de menú de un food truck.
- Atkinson Hyperlegible (400/700): todo lo demás, legible a un brazo de distancia en una cocina con prisa.

**Layout**

```
Pedidos del 28 de agosto           [Todos|Camión 1|Camión 2] [Crear pedido]
2 pedidos esperan a su cliente.
████████████████████████ riel ████████████████████████████████████████████
Recibido 2     | En preparación 2 | ▀▀▀ Listo para recoger 2 | Entregado 1
┌──#1─Cam 1─┐  | ┌──#2──────────┐ | ┌──#4───────────┐        | (atenuado)
│ Ana Perez │  | │ ...          │ | │ ...           │        |
│ 1× Taco   │  | │[Marcar listo]│ | │[Entregar]     │        |
└/\/\/\/\/\/┘  | └/\/\/\/\/\/\/\┘ | └/\/\/\/\/\/\/\/┘        |
```

Alineación a la izquierda; los carriles siguen el orden real del pedido (Recibido → Entregado).

**Principios**
1. La pieza memorable es el riel de comandas: papel con borde troquelado y gancho. Todo lo demás es sobrio.
2. Cada botón dice lo que pasa: "Empezar a preparar", "Marcar como listo", "Entregar al cliente".
3. El color nunca va solo: cada camión dice su nombre y cada carril su estado y su cantidad.
4. Los vacíos orientan: "Nada esperando. Los pedidos listos aparecen aquí."

## Revisión contra el brief (paso 2)

La primera idea fue un tablero kanban con tarjetas blancas redondeadas y sombra suave: es el "kit de tarjetas SaaS" que la skill marca como genérico. Lo cambiamos por comandas de papel colgadas de un riel, que vienen del mundo real de una cocina de comida rápida. También quitamos etiquetas en mayúsculas sostenidas, tipografía monoespaciada para datos y tarjetas de estadísticas con números grandes.

## Diferencias medibles

| | Antes | Después |
|---|---|---|
| Estructura | Encabezado con degradado, 4 tarjetas de estadísticas y tabla | Riel con 4 carriles en el orden del flujo |
| Qué espera al cliente | Hay que leer la columna Estado fila por fila | Carril ámbar con contador y resumen arriba |
| Estados | Valores de la API en inglés (`Picked Up`) | En español, como los lee el equipo |
| Acciones | Botón "Editar" igual en todas las filas | Un botón por pedido con el siguiente paso |
| Filtro por camión | No existe | Selector Todos / Camión 1 / Camión 2 |
| Accesibilidad | Badges que dependen solo del color | Foco visible, `aria-pressed`, movimiento reducido |
| Móvil | Tabla que se desborda | Carriles con desplazamiento horizontal |
