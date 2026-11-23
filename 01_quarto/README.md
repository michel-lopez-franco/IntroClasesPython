# 01 · Quarto con Python

Guía rápida y ejemplos básicos para crear documentos, reportes y presentaciones
que mezclan texto y código Python usando [Quarto](https://quarto.org).

## Contenido

```
01_quarto/
├── _quarto.yml                     # Convierte la carpeta en proyecto (sitio web)
├── index.qmd                       # Página de inicio del sitio
├── guia_rapida.qmd                 # Guía de referencia (empieza aquí)
└── ejemplos/
    ├── 01_hola_quarto.qmd          # Primer documento: Markdown + código
    ├── 02_opciones_celdas.qmd      # echo, eval, include, código en línea
    ├── 03_graficas.qmd             # Matplotlib, Plotly, referencias a figuras
    ├── 04_tablas_ecuaciones.qmd    # Tablas, LaTeX, callouts, columnas
    ├── 05_clases_python.qmd        # Documentar clases (POO) + diagrama Mermaid
    ├── 06_presentacion.qmd         # Presentación Reveal.js
    ├── 07_animaciones_plotly.qmd   # Animaciones Plotly: frames, Play/Pausa, slider
    └── 08_html_js.qmd              # HTML+CSS+JS crudo, HTML desde Python, Observable JS
```

## Requisitos

- Quarto instalado (`quarto --version`)
- Dependencias del proyecto: `uv sync` (incluye `jupyter`, `matplotlib`, `plotly`)

## Uso

Desde la raíz del repositorio:

```bash
# Todo el proyecto de una vez
uv run quarto render 01_quarto     # genera todos los HTML en 01_quarto/_site/
uv run quarto preview 01_quarto    # abre el sitio con menú lateral y recarga al guardar

# Un solo archivo
uv run quarto preview 01_quarto/ejemplos/01_hola_quarto.qmd
uv run quarto render  01_quarto/ejemplos/01_hola_quarto.qmd
```

**`render` vs `preview`:** `render` genera los archivos una vez y termina (para la
versión final). `preview` renderiza, abre el navegador y se queda vigilando: cada vez
que guardas, recarga la página sola (para cuando estás escribiendo). Se detiene con `Ctrl + C`.
Más detalle en la sección *render vs preview* de `guia_rapida.qmd`.

Los archivos generados (`_site/`, `.quarto/`) se ignoran en git (ver `.gitignore`).
