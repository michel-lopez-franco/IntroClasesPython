# Plan: sitio del curso de POO en Python con Quarto

> **Cómo usar este archivo:** ábrelo en un agente (Claude Code) desde la raíz del repositorio y
> pídele: *"Lee CLAUDE.md y ejecuta PLAN_CURSO_QUARTO.md fase por fase. Al terminar cada fase,
> verifica, resume lo hecho y espera mi confirmación antes de seguir."*

---

## 1. Objetivo

Convertir los 10 notebooks de `src/` en un **sitio web del curso hecho con Quarto (tipo Book)**,
que sirva para:

- **Estudiar de forma autónoma**: lectura clara, ejercicios con solución plegable, código
  ejecutable en el navegador sin instalar nada.
- **Dar la clase presencial**: una presentación Reveal.js por tema, generada en el mismo proyecto.

Decisión ya tomada: **Quarto, no React.** El contenido es lo central; la interactividad se añade
sólo donde ayuda a entender un concepto (Pyodide, Python Tutor, Mermaid, alguna animación OJS).

## 2. Contexto (leer antes de empezar)

- `CLAUDE.md` — estructura, comandos (`uv run quarto …`), convenciones y verificación.
- `src/*.ipynb` — contenido fuente. Cada notebook sigue el patrón: título → "¿Qué es…?" →
  "Analogía del mundo real" → ejemplos de código progresivos. **No se modifican.**
- `01_quarto/` — guía y ejemplos de Quarto ya probados; reutilizar sus técnicas
  (callouts, `code-fold`, Mermaid, `embed`, revealjs, OJS, Plotly con `graph_objects`).
- `utils/classDiagram.mmd`, `utils/clase.md` — diagramas Mermaid existentes (Animal/Perro/Gato,
  Vehiculo/Coche/Moto) reutilizables.
- Público: estudiantes de maestría (propedéutico). Idioma: español. Tono: claro y directo.

| # | Notebook | Tema | Salidas guardadas |
|---|---|---|---|
| 01 | `01_Introduccion_Clases_Objetos` | Clases y objetos, instanciación | sí |
| 02 | `02_Atributos_Metodos` | Atributos, métodos, `self` | sí |
| 03 | `03_Constructor_Self` | `__init__`, `self`, valores por defecto | sí |
| 04 | `04_Herencia` | Herencia, `super()` | no |
| 05 | `05_Encapsulamiento_Propiedades` | Público/protegido/privado, name mangling, `@property` | no |
| 06 | `06_Polimorfismo` | Polimorfismo, duck typing | no |
| 07 | `07_Metodos_Especiales` | `__str__`, `__repr__`, operadores | no |
| 08 | `08_Composicion_Agregacion` | Composición vs agregación | no |
| 09 | `09_Clases_Abstractas` | `abc`, clases abstractas, interfaces | no |
| 10 | `10_Proyecto_Integrador` | Tienda en línea (integra todo) | no |

## 3. Estructura objetivo

```
curso/
├── _quarto.yml            # project: book; lang: es; formato html (+ live-html si aplica)
├── .gitignore             # _book/, _site/, .quarto/, *_files/, __pycache__/
├── index.qmd              # Presentación: objetivos, requisitos, cómo usar el sitio
├── 01_clases_objetos.qmd
├── 02_atributos_metodos.qmd
├── …                      # un capítulo por notebook, nombres cortos en snake_case
├── 10_proyecto_integrador.qmd
├── ejercicios/            # (opcional) si los ejercicios crecen demasiado
├── slides/
│   ├── 01_clases_objetos.qmd   # format: revealjs (o un único archivo por bloque de temas)
│   └── …
└── recursos/
    ├── diagramas/         # .mmd reutilizables
    └── referencia.qmd     # hoja resumen de sintaxis POO (apéndice)
```

`curso/` es un proyecto Quarto independiente (tiene su propio `_quarto.yml`); no tocar el
`_quarto.yml` raíz.

## 4. Fases

### Fase 0 — Preparación
- Crear `curso/` con `_quarto.yml` (book, `lang: es`, tema limpio, `toc`, `number-sections`,
  búsqueda) e `index.qmd`.
- Ejecutar los notebooks 04–10 en una copia temporal (no en `src/`) para detectar errores de
  código existentes. **Reportar** cualquier celda que falle; no corregir `src/` sin permiso.
- ✅ Hecho cuando: `uv run quarto render curso` genera el libro vacío con índice.

### Fase 1 — Capítulos base (contenido)
- `uv run quarto convert` cada notebook a una copia `.qmd` en `curso/` (nunca sobre `src/`).
- Limpiar cada capítulo: título en el YAML, encabezados coherentes, opciones `#|` donde convenga,
  `label`/`fig-cap` en figuras. Conservar íntegros explicaciones y ejemplos del original.
- Las celdas que fallan a propósito (p. ej. acceso a atributo privado, instanciar una clase
  abstracta) llevan `#| error: true`.
- Agregar en cada capítulo:
  - Callout **"Objetivos"** al inicio y **"Resumen"** al final.
  - Un **diagrama de clases Mermaid** cuando haya relaciones entre clases (04, 06, 08, 09, 10 como mínimo).
  - Sección **"Ejercicios"** (2–4 por capítulo) con solución en
    `::: {.callout-tip collapse="true"}`.
- ✅ Hecho cuando: el libro completo renderiza sin errores y cada capítulo tiene objetivos,
  resumen, ejercicios con solución y (si aplica) diagrama.

### Fase 2 — Código ejecutable en el navegador
- Instalar la extensión **quarto-live** (`quarto add r-wasm/quarto-live`, en `curso/`) y
  **verificar la sintaxis actual en su documentación** (formato `live-html`, celdas
  ```` ```{pyodide} ````). Si no es viable, alternativa: extensión `quarto-pyodide`
  (coatless-quarto/pyodide).
- Convertir a celdas editables **sólo** los ejemplos clave de cada capítulo (2–3 por capítulo)
  y los ejercicios "prueba tú". El resto queda como celdas `{python}` normales.
- Verificar que los paquetes usados funcionen en Pyodide (stdlib sí; `matplotlib` sí; revisar
  cualquier otro).
- ✅ Hecho cuando: renderiza sin errores y el HTML contiene las celdas interactivas.
  Indicar al usuario que debe probarlas en el navegador (`uv run quarto preview curso`).

### Fase 3 — Visualizaciones para conceptos difíciles
- **Python Tutor** incrustado (iframe de `pythontutor.com/iframe-embed.html` con el código
  codificado en la URL; verificar el formato actual) en los capítulos 01–03 para mostrar
  objetos, referencias y `self`, y en 08 para composición.
- **Una o dos** animaciones con Observable JS o HTML/JS (ver `01_quarto/ejemplos/08_html_js.qmd`)
  sólo si aportan; candidatas: recorrido del MRO / `super()` en herencia (04) y despacho
  polimórfico (06). No añadir animaciones decorativas.
- ✅ Hecho cuando: los capítulos indicados las incluyen y el render no falla.

### Fase 4 — Diapositivas
- Una presentación Reveal.js por capítulo en `curso/slides/` (o agrupadas por módulo):
  10–15 diapositivas, una idea por diapositiva, código corto, diagramas Mermaid, notas del
  presentador (`::: {.notes}`) con lo que se explica oralmente.
- Enlazar cada presentación desde su capítulo (callout "Diapositivas de este tema").
- ✅ Hecho cuando: todas las presentaciones renderizan y están enlazadas.

### Fase 5 — Cierre
- Apéndice `recursos/referencia.qmd`: hoja resumen de sintaxis POO.
- En cada capítulo, botón/enlace "Abrir en Colab" al notebook original (requiere URL del
  repositorio en GitHub: **preguntar al usuario**).
- Corregir los enlaces del `README.md` raíz (hoy apuntan a `01_…ipynb` en la raíz y los
  notebooks están en `src/`) y añadir sección de cómo ver/renderizar el sitio.
- Publicación en GitHub Pages (`quarto publish gh-pages`): **sólo con confirmación del usuario**.

## 5. Decisiones abiertas (preguntar al usuario si bloquean)

1. **Modalidad** del curso (presencial / en línea / autodidacta). Por defecto: mixto
   (sitio para estudiar + diapositivas para clase). Si es sólo presencial, priorizar Fase 4
   sobre Fase 2.
2. ¿`src/*.ipynb` sigue siendo la fuente de verdad o, tras la Fase 1, los `.qmd` de `curso/`
   pasan a serlo? Por defecto: los `.qmd` pasan a ser la fuente; los notebooks quedan como
   versión para Colab.
3. URL del repositorio en GitHub (para enlaces a Colab y publicación).
4. Nivel de los ejercicios (básico / intermedio) y si se quieren soluciones visibles.

## 6. Restricciones

- No modificar `src/`, `01_quarto/` ni `_quarto.yml` raíz salvo petición explícita.
- No usar React ni herramientas de build de JavaScript (npm, etc.).
- No agregar `pandas` salvo que el usuario lo pida; para gráficas, `matplotlib` o
  `plotly.graph_objects`.
- Todo el contenido en español.
- No hacer commit, push ni publicar sin pedirlo.
- Trabajar por fases y detenerse al final de cada una para confirmación.

## 7. Criterios de terminado (global)

- `uv run quarto render curso` termina sin errores.
- 10 capítulos + índice + apéndice, navegables desde la barra lateral, con búsqueda.
- Cada capítulo: objetivos, contenido del notebook original, diagrama (si aplica),
  ejercicios con solución, enlace a diapositivas.
- Ejemplos clave ejecutables en el navegador.
- Salidas generadas excluidas de git.
- Resumen final al usuario: qué se hizo, qué se verificó, qué falta probar manualmente en el
  navegador y qué decisiones quedaron pendientes.
