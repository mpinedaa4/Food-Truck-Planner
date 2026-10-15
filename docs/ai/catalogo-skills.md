# Catálogo de skills — Food Truck Planner

Laboratorio Semana 13 · Proyecto Trayectoria en Desarrollo de Software · EAFIT

## Contexto

El proyecto es una API en **Python + FastAPI + Pydantic** con datos mock en memoria y pruebas con **Pytest + HTTPX** (ver `AGENTS.md`). Hoy tiene `POST /pedidos`, `GET /pedidos` y `PATCH /pedidos/{id}/estado`, con la regla de negocio de que un pedido solo se crea si para su fecha hay una ruta con camión asignado. El repositorio no tiene todavía workflow de CI.

Lo que necesitamos de las skills:

- Especificar cambios sobre código que ya existe (por eso elegimos **OpenSpec**).
- Implementar endpoints respetando las restricciones de `AGENTS.md`: sin base de datos, sin autenticación, sin dependencias nuevas.
- Escribir pruebas de éxito y de rechazo antes del código.
- Revisar el PR contra la spec y contra `AGENTS.md`, y tener CI en verde.

## Fuentes consultadas

| Fuente | Tipo | Qué tomamos |
|---|---|---|
| [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) y [anthropics/skills](https://github.com/anthropics/skills) | Oficial | `frontend-design`; `claude-security` (descartada) |
| [skills.sh](https://skills.sh) | Directorio | Ranking y fichas de mattpocock/skills, obra/superpowers, wshobson/agents, trailofbits/skills y malikasadjaved/skills |
| [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | Repositorio del framework SDD | `openspec-propose` |
| Repositorios de cada publicador en GitHub | Repositorio | Lectura completa de `SKILL.md`, referencias y `scripts/` |

Método de revisión: clonamos cada repositorio, leímos el `SKILL.md` completo, sus archivos de referencia y sus scripts, buscamos referencias a `.env`, llamadas de red (`curl`, `wget`, `requests`, `urlopen`) y caracteres Unicode invisibles (rangos U+200B–U+200F, U+202A–U+202E, U+2060–U+2064, U+FEFF y etiquetas U+E0000–U+E007F). Ninguna de las 14 skills revisadas tiene caracteres invisibles. La fecha de actualización es el último commit que tocó la carpeta de la skill, revisado el 15 de octubre de 2026.

## Resumen

| # | Skill | Categoría | Fase SDD | Veredicto |
|---|---|---|---|---|
| 1 | openspec-propose | Especificar y planear | spec, plan | Adoptar |
| 2 | grill-me / grilling | Especificar y planear | spec | Adoptar |
| 3 | fastapi-templates | Implementar | código | Adaptar |
| 4 | frontend-design | Implementar (UX/UI) | plan, código | Adoptar |
| 5 | test-driven-development | Probar | tests | Adoptar |
| 6 | python-testing-patterns | Probar | tests | Adoptar |
| 7 | differential-review | Revisar y seguridad | revisión | Adoptar |
| 8 | code-review | Revisar y seguridad | revisión | Adaptar |
| 9 | github-actions-templates | Calidad o libre | revisión (CI) | Adaptar |
| 10 | verification-before-completion | Calidad o libre | tests, revisión | Adoptar |
| ★ | **food-truck-endpoint** (propia) | Implementar + probar | código, tests | Creada en `.claude/skills/` |

Descartadas: `fastapi-best-practices`, `claude-security`, `writing-plans`.

---

## 1. Especificar y planear

## Skill: openspec-propose
Fuente: https://github.com/Fission-AI/OpenSpec/tree/main/skills/openspec-propose · Licencia: MIT
Actualizada: 2026-09-16 · Publicador: Fission AI
Fase SDD: spec | plan

Qué hace (2 líneas): A partir de una descripción crea un cambio en `openspec/changes/<nombre>/` con `proposal.md`, specs delta, `design.md` y `tasks.md`. Se limita a planear: no edita código hasta que se pide el flujo de aplicar.

Revisión de seguridad:
- ¿Tiene scripts? No. Solo ejecuta el CLI `openspec` (está restringido a `Bash(openspec:*)` en `allowed-tools`).
- ¿Lee .env o envía datos fuera? No.
- ¿Instrucciones raras o caracteres invisibles? No. Trata el `context` del `config.yaml` como datos y no como autoridad, lo cual es una buena práctica contra inyección.

Veredicto: Adoptar
Por qué: Es el framework que la presentación recomienda para código existente, y genera justo los artefactos (spec, plan, tareas) que pide el paso 3 del laboratorio. Requiere `npm install -g @fission-ai/openspec` y `openspec init` una vez.

## Skill: grill-me (invoca a grilling)
Fuente: https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me · Licencia: MIT
Actualizada: 2026-10-07 (grilling) · Publicador: Matt Pocock
Fase SDD: spec

Qué hace (2 líneas): Entrevista al usuario por rondas sobre un plan, con preguntas numeradas y una respuesta recomendada para cada una. Termina cuando no quedan decisiones abiertas.

Revisión de seguridad:
- ¿Tiene scripts? No.
- ¿Lee .env o envía datos fuera? No.
- ¿Instrucciones raras o caracteres invisibles? No. `grill-me` tiene `disable-model-invocation: true`, así que solo se activa con `/grill-me`.

Veredicto: Adoptar
Por qué: El `MVP Scope.md` tiene seis puntos en UNKNOWN (roles, cancelación de pedidos, historial). Antes de `openspec-propose` sirve para cerrar esas decisiones con el equipo. Es una de las skills más instaladas de skills.sh.

---

## 2. Implementar

## Skill: fastapi-templates
Fuente: https://github.com/wshobson/agents/tree/main/plugins/api-scaffolding/skills/fastapi-templates · Licencia: MIT
Actualizada: 2026-10-15 · Publicador: Seth Hobson (wshobson/agents), último cambio de un contribuidor externo
Fase SDD: código

Qué hace (2 líneas): Da la estructura de un proyecto FastAPI de producción: capas de rutas, servicios y repositorios, inyección de dependencias y pruebas con `dependency_overrides`. Sus ejemplos usan SQLAlchemy async, PostgreSQL y JWT.

Revisión de seguridad:
- ¿Tiene scripts? No, solo `references/details.md` con ejemplos.
- ¿Lee .env o envía datos fuera? El agente no. El código de ejemplo configura `pydantic-settings` para leer `.env`.
- ¿Instrucciones raras o caracteres invisibles? No.

Veredicto: Adaptar
Por qué: La separación rutas/servicios/datos coincide con nuestro proyecto, pero instalarla tal cual empujaría al agente a crear base de datos, autenticación y `/api/v1`, que `AGENTS.md` prohíbe. La adaptamos en nuestra skill propia `food-truck-endpoint`. Se actualizó el mismo día de la revisión: hay que volver a leerla antes de usarla.

## Skill: frontend-design
Fuente: https://github.com/anthropics/skills/tree/main/skills/frontend-design · Licencia: Apache 2.0
Actualizada: 2026-09-03 · Publicador: Anthropic
Fase SDD: plan | código

Qué hace (2 líneas): Guía de diseño UX/UI: antes de escribir la interfaz, el agente define un plan (paleta, tipografías, layout y principios), lo revisa contra los patrones genéricos y después construye y critica con capturas. También da reglas de textos de interfaz: botones que dicen lo que hacen y vacíos que orientan.

Revisión de seguridad:
- ¿Tiene scripts? No. Solo `SKILL.md` y `LICENSE.txt`.
- ¿Lee .env o envía datos fuera? No.
- ¿Instrucciones raras o caracteres invisibles? No. Sugiere usar la memoria del usuario como pista del contexto del cliente, que es inofensivo.

Veredicto: Adoptar
Por qué: Los mockups del proyecto (Dispatcher, Kitchen kanban, Truck Operator) van a necesitar pantallas, y sin guía el agente produce plantillas genéricas. La probamos en la demo de `docs/ai/demo-ux/`: mismo prompt y mismos datos, antes y después. `AGENTS.md` prohíbe modificar el frontend en las tareas de backend, así que esta skill se usa solo en tareas de interfaz.

> Reemplazó a `api-design-principles` (wshobson/agents, MIT), que también era útil pero se solapaba con las convenciones REST que ya fija `AGENTS.md`.

---

## 3. Probar

## Skill: test-driven-development
Fuente: https://github.com/obra/superpowers/tree/main/skills/test-driven-development · Licencia: MIT
Actualizada: 2026-09-18 · Publicador: Jesse Vincent (obra/superpowers)
Fase SDD: tests

Qué hace (2 líneas): Obliga al ciclo rojo-verde-refactor: primero una prueba que falle por la razón correcta, luego el código mínimo. Exige correr la suite completa antes de decir que terminó.

Revisión de seguridad:
- ¿Tiene scripts? No.
- ¿Lee .env o envía datos fuera? No.
- ¿Instrucciones raras o caracteres invisibles? No. El tono es muy imperativo ("borra el código y empieza de nuevo"), pero es metodología, no un riesgo.

Veredicto: Adoptar
Por qué: `AGENTS.md` exige prueba del caso exitoso y del rechazo para cada cambio de lógica; esta skill hace que el agente las escriba antes del código y no después.

## Skill: python-testing-patterns
Fuente: https://github.com/wshobson/agents/tree/main/plugins/python-development/skills/python-testing-patterns · Licencia: MIT
Actualizada: 2026-09-28 · Publicador: Seth Hobson (wshobson/agents)
Fase SDD: tests

Qué hace (2 líneas): Patrones de Pytest: fixtures en `conftest.py`, parametrización, mocks, nombres de pruebas y aislamiento. Las referencias cubren pruebas async y de API.

Revisión de seguridad:
- ¿Tiene scripts? No.
- ¿Lee .env o envía datos fuera? No. Las menciones a `requests.get` son ejemplos de cómo mockear llamadas HTTP.
- ¿Instrucciones raras o caracteres invisibles? No.

Veredicto: Adoptar
Por qué: Nuestras pruebas modifican listas mock globales (`mock_pedidos`); los patrones de fixtures y aislamiento ayudan a que no dependan del orden. `@pytest.mark.parametrize` sirve para probar los cuatro estados válidos y los inválidos en una sola prueba.

---

## 4. Revisar y seguridad

## Skill: differential-review
Fuente: https://github.com/trailofbits/skills/tree/main/plugins/differential-review/skills/differential-review · Licencia: CC BY-SA 4.0
Actualizada: 2026-09-16 · Publicador: Trail of Bits
Fase SDD: revisión

Qué hace (2 líneas): Revisión de seguridad de un diff o PR: clasifica cada archivo por riesgo, usa `git blame` para ver si se quitaron validaciones, calcula el radio de impacto y revisa cobertura de pruebas. Siempre deja un reporte en Markdown.

Revisión de seguridad:
- ¿Tiene scripts? No. Usa `Bash` para comandos `git` y escribe un archivo de reporte.
- ¿Lee .env o envía datos fuera? No. `agents/openai.yaml` es solo metadatos de presentación.
- ¿Instrucciones raras o caracteres invisibles? No.

Veredicto: Adoptar
Por qué: Antes de integrar el PR a `main` detecta lo más peligroso para nosotros: quitar la validación de "ruta con camión asignado" o de los estados válidos. Ojo con la licencia: si copiamos su texto a otra skill hay que atribuir y compartir con la misma licencia.

## Skill: code-review
Fuente: https://github.com/mattpocock/skills/tree/main/skills/engineering/code-review · Licencia: MIT
Actualizada: 2026-10-07 · Publicador: Matt Pocock
Fase SDD: revisión

Qué hace (2 líneas): Revisa el diff contra un punto fijo en dos ejes separados: estándares del repo y cumplimiento de la spec. Corre dos subagentes en paralelo y no mezcla sus hallazgos.

Revisión de seguridad:
- ¿Tiene scripts? No. Ejecuta `git diff`, `git log` y `git rev-parse`.
- ¿Lee .env o envía datos fuera? No.
- ¿Instrucciones raras o caracteres invisibles? No.

Veredicto: Adaptar
Por qué: Los dos ejes encajan perfecto con SDD (¿cumple la spec? ¿cumple `AGENTS.md`?). Pero asume un issue tracker configurado con `/setup-matt-pocock-skills`; la adaptamos para que tome la spec de `openspec/changes/<cambio>/` y los estándares de `AGENTS.md`.

---

## 5. Calidad o libre

## Skill: github-actions-templates
Fuente: https://github.com/wshobson/agents/tree/main/plugins/cicd-automation/skills/github-actions-templates · Licencia: MIT
Actualizada: 2026-09-28 · Publicador: Seth Hobson (wshobson/agents)
Fase SDD: revisión (CI)

Qué hace (2 líneas): Plantillas de workflows de GitHub Actions para pruebas, construcción de imágenes Docker y despliegue. Cubre matrices, caché y permisos mínimos.

Revisión de seguridad:
- ¿Tiene scripts? No.
- ¿Lee .env o envía datos fuera? No. Los ejemplos de despliegue usan `secrets.GITHUB_TOKEN` y suben a registros, que no necesitamos.
- ¿Instrucciones raras o caracteres invisibles? No.

Veredicto: Adaptar
Por qué: El paso 5 exige el PR con CI en verde y el repo no tiene workflow. La plantilla de pruebas está escrita para Node; la adaptamos a Python (`actions/setup-python`, `pip install -r requirements.txt`, `pytest`) y dejamos fuera Docker y despliegue.

## Skill: verification-before-completion
Fuente: https://github.com/obra/superpowers/tree/main/skills/verification-before-completion · Licencia: MIT
Actualizada: 2026-07-23 · Publicador: Jesse Vincent (obra/superpowers)
Fase SDD: tests | revisión

Qué hace (2 líneas): Prohíbe que el agente diga "listo" o "pasan las pruebas" sin haber corrido el comando en ese mismo paso y leído su salida. Aplica antes de commits y PRs.

Revisión de seguridad:
- ¿Tiene scripts? No.
- ¿Lee .env o envía datos fuera? No.
- ¿Instrucciones raras o caracteres invisibles? No.

Veredicto: Adoptar
Por qué: En la fase 4 se genera código tarea por tarea; esta skill evita que el agente marque una tarea como terminada sin `pytest` en verde.

---

## Skill propia: food-truck-endpoint

Ubicación: `.claude/skills/food-truck-endpoint/SKILL.md`
Origen: adaptada de `fastapi-templates` y `test-driven-development` (ambas MIT).
Fase SDD: código | tests

Qué hace: Guía al agente para agregar o cambiar un endpoint siguiendo `AGENTS.md`: ruta en `main.py`, lógica y modelos en `src/services/`, datos en `mock_data.py`, pruebas de éxito y rechazo antes del código, y `pytest -q` en verde antes de terminar.

Qué cambiamos respecto a las originales: quitamos base de datos, SQLAlchemy, JWT, CORS y `/api/v1`; fijamos los códigos de estado, la forma de los errores, los estados válidos y la regla de la ruta con camión; agregamos convenciones de ramas y commits.

---

## Conclusiones y descartes

Lo que encontramos al leerlas:

- Ninguna de las skills revisadas tenía caracteres invisibles ni enviaba datos fuera, pero varias **asumen un contexto distinto al nuestro**: base de datos, JWT, Node o un issue tracker. Instaladas sin leer, el agente habría violado `AGENTS.md`.
- **Pasar las auditorías del directorio no basta.** `fastapi-best-practices` pasó los tres chequeos automáticos de skills.sh y aun así la descartamos.
- **La licencia también es parte de la revisión.** Encontramos una skill sin licencia y otra con licencia propietaria dentro de un repositorio Apache 2.0.
- Una skill se actualizó el mismo día de la revisión: la revisión vale para una versión concreta.

### Descartada: fastapi-best-practices
Fuente: https://github.com/malikasadjaved/skills · Licencia: **ninguna** · Actualizada: 2026-05-09 · Publicador: Malik Asad Javed Awan
Motivos: el repositorio no tiene licencia, así que no podemos copiarla ni adaptarla legalmente. Recomienda `python-jose` para JWT y trae plantillas con Qdrant, Redis, `.env` y una URL de producción de otro proyecto. Tiene 1 instalación en skills.sh. Pasó las auditorías automáticas del directorio, lo que muestra que esas auditorías no reemplazan la lectura.

### Descartada: claude-security
Fuente: https://github.com/anthropics/claude-plugins-official/tree/main/plugins/claude-security · Licencia: **propietaria** ("All rights reserved", aunque el repositorio raíz es Apache 2.0) · Actualizada: 2026-09-25 · Publicador: Anthropic
Motivos: requiere la herramienta Workflow de Claude Code, que no todos tenemos; instala hooks que se ejecutan en cada `git push` y después de sus scripts; y es un escaneo profundo, desproporcionado para una API de cuatro endpoints. Para nuestro PR basta `differential-review`.

### Descartada: writing-plans
Fuente: https://github.com/obra/superpowers/tree/main/skills/writing-plans · Licencia: MIT · Actualizada: 2026-09-25 · Publicador: Jesse Vincent
Motivos: es buena, pero duplica el `tasks.md` que ya genera OpenSpec, guarda los planes en `docs/superpowers/plans/` y depende de otras skills de superpowers (`subagent-driven-development`, `executing-plans`). Usarla junto con OpenSpec dejaría dos planes distintos para el mismo cambio.

---

## Guion del showcase (5 minutos)

1. **Contexto (45 s).** API FastAPI de pedidos para food trucks, sin base de datos, con reglas en `AGENTS.md`. Necesitamos skills que respeten esas restricciones.
2. **Las 10 skills (2 min).** Mostrar la tabla resumen: dos por categoría y el veredicto de cada una.
3. **Descartes (45 s).** Las tres descartadas y la lección: auditoría automática ≠ revisión, y la licencia cuenta.
4. **Demo (1,5 min)** con la skill propia `food-truck-endpoint`:
   - Problema que resuelve: que el agente agregue endpoints sin romper `AGENTS.md` y con pruebas primero.
   - De dónde viene: adaptada por nosotros de `fastapi-templates` (wshobson) y `test-driven-development` (obra).
   - Prompt con slash:
     `/food-truck-endpoint Agrega GET /rutas que liste las rutas y permita filtrar por fecha. Una fecha con formato inválido debe responder 400.`
   - Prompt sin la skill:
     `Agrega GET /rutas que liste las rutas y permita filtrar por fecha. Una fecha con formato inválido debe responder 400. No uses la skill food-truck-endpoint.`
   - Qué comparar: si escribió las pruebas antes del código, si puso la lógica en `src/services/`, si probó el caso de rechazo, si corrió `pytest -q` y si agregó algo no pedido (dependencias, `/api/v1`, base de datos).
