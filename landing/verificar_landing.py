"""Verificación de la landing final con Playwright (skill webapp-testing de Anthropic).

No es parte de la suite de la API: el nombre no empieza por test_ para que pytest no lo recoja
y no agrega dependencias a requirements.txt.

Uso (con Playwright instalado aparte):
    python landing/verificar_landing.py
"""

import pathlib
import sys

from playwright.sync_api import sync_playwright

PAGINA = (pathlib.Path(__file__).parent / "final" / "index.html").resolve().as_uri()
fallas = []


def revisar(condicion, mensaje):
    print(("OK   " if condicion else "FALLA") + "  " + mensaje)
    if not condicion:
        fallas.append(mensaje)


with sync_playwright() as p:
    navegador = p.chromium.launch()
    for ancho in (1440, 1024, 768, 390):
        pagina = navegador.new_page(viewport={"width": ancho, "height": 900})
        errores = []
        pagina.on("pageerror", lambda e: errores.append(str(e)))
        pagina.goto(PAGINA)
        pagina.wait_for_timeout(400)
        revisar(pagina.evaluate("document.documentElement.scrollWidth") == ancho, f"{ancho}px: sin scroll horizontal")
        revisar(not errores, f"{ancho}px: sin errores de JavaScript")

    pagina = navegador.new_page(viewport={"width": 1440, "height": 900})
    pagina.goto(PAGINA)

    # Selector de camión: cambia el letrero y el estado
    pagina.click("#tab-2")
    revisar(pagina.inner_text("#s-street") == "Parque de los Deseos", "Camión 2 muestra su esquina")
    revisar(pagina.get_attribute("#tab-2", "aria-selected") == "true", "Camión 2 queda seleccionado")
    pagina.focus("#tab-2")
    pagina.keyboard.press("ArrowLeft")
    revisar(pagina.inner_text("#s-street") == "Calle 10", "Flecha izquierda vuelve al Camión 1")
    estado = pagina.inner_text("#s-status")
    revisar(any(t in estado for t in ("Abierto ahora", "Abre hoy", "Cerrado por hoy")), f"Estado en vivo: {estado}")

    # Enlace directo
    pagina.goto(PAGINA + "#camion-2")
    revisar(pagina.inner_text("#s-street") == "Parque de los Deseos", "#camion-2 abre el Camión 2")

    # Acordeón
    pagina.click("#b3")
    revisar(pagina.get_attribute("#b3", "aria-expanded") == "true", "Acordeón abre 'Listo'")
    revisar(pagina.get_attribute("#b1", "aria-expanded") == "false", "Acordeón cierra el panel anterior")

    # Consulta de pedido: éxito y rechazos
    casos = [
        ("4", "#r-t", "Pedido #4 de Jorge: Listo para recoger"),
        ("2", "#r-t", "Pedido #2 de Luis: En preparación"),
        ("99", "#n-err", "No encontramos el pedido #99"),
        ("abc", "#n-err", "Usa solo números"),
        ("", "#n-err", "Escribe tu número de pedido"),
    ]
    for valor, selector, esperado in casos:
        pagina.fill("#n", valor)
        pagina.click("#go")
        pagina.wait_for_timeout(700)
        revisar(esperado in pagina.inner_text(selector), f"Consulta '{valor}' → {esperado}")
    revisar(pagina.get_attribute("#n", "aria-invalid") == "true", "El campo queda marcado como inválido tras un error")

    pagina.fill("#n", "4")
    pagina.click("#go")
    pagina.wait_for_timeout(700)
    revisar(pagina.locator("#r-track li[aria-current=step]").inner_text() == "Listo", "La barra marca el paso actual")

    # Movimiento reducido: el contenido se ve sin desplazamientos
    contexto = navegador.new_context(reduced_motion="reduce", viewport={"width": 1440, "height": 900})
    quieta = contexto.new_page()
    quieta.goto(PAGINA)
    revisar(quieta.evaluate("[...document.querySelectorAll('.rise')].every(e => getComputedStyle(e).transform === 'none')"),
            "Con movimiento reducido no hay desplazamientos")
    navegador.close()

print(f"\n{len(fallas)} falla(s)")
sys.exit(1 if fallas else 0)
