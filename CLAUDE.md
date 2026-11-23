# CLAUDE.md

Contexto permanente del repositorio para agentes de código.

## Qué es este repositorio

Material didáctico del curso **Introducción a la Programación Orientada a Objetos en Python**
(propedéutico de maestría, CUCEI). Todo el contenido y la comunicación con el usuario van en
**español**.

## Estructura

```
src/          10 notebooks del curso (01_Introduccion_Clases_Objetos … 10_Proyecto_Integrador).
              FUENTE ORIGINAL del contenido: no modificarlos salvo petición explícita.
              Sólo 01–03 tienen salidas guardadas; 04–10 están sin ejecutar.
utils/        Notas y diagramas sueltos (clase.md, classDiagram.mmd, info.drawio).
01_quarto/    Guía rápida de Quarto + 9 ejemplos (proyecto Quarto tipo website, con su _quarto.yml).
              Sirve de REFERENCIA de estilo y técnicas (callouts, Plotly, OJS, embed, revealjs).
quartoejs/    Prueba inicial de Quarto (hola.qmd).
_quarto.yml   Proyecto raíz tipo `default` (no lo conviertas en website/book).
pyproject.toml / uv.lock   Dependencias, gestionadas con uv.
```

Cada carpeta con su propio `_quarto.yml` es un proyecto Quarto independiente (gana el más cercano).

## Herramientas y comandos

- Python ≥ 3.13 gestionado con **uv**. Ejecuta siempre a través de `uv run`.
- Dependencias actuales: `jupyter`, `matplotlib`, `notebook`, `plotly`. **No hay pandas**:
  usa `plotly.graph_objects` en lugar de `plotly.express`. Agrega paquetes con `uv add <paquete>`,
  nunca con `pip install`.
- Quarto 1.11 instalado en `/Applications/quarto/bin/quarto`.

```bash
uv sync                                   # instalar dependencias
uv run quarto render <carpeta-proyecto>   # renderizar un proyecto completo
uv run quarto render <archivo.qmd>        # un archivo
uv run quarto preview <carpeta|archivo>   # vista previa en vivo (no termina: no usar en verificaciones)
uv run quarto convert <nb.ipynb>          # notebook → .qmd
```

## Convenciones

- Celdas de código en `.qmd`: ```` ```{python} ```` con opciones `#|` (`label`, `fig-cap`, `echo`…).
  Etiquetas de figura `fig-…`, tabla `tbl-…`, ecuación `eq-…` para referencias cruzadas.
- Poner `lang: es` en el `_quarto.yml` de cada proyecto.
- Para mostrar sintaxis de Quarto sin que se ejecute:
  código en línea → `` `{{python}} expr` ``; shortcodes → `{{{< embed … >}}}`.
- Si se generan notebooks a mano, `source` como lista de líneas y cada celda con `id`.
- Las salidas generadas (`_site/`, `*_files/`, `.quarto/`, `*.html`) no se versionan:
  cada proyecto Quarto lleva un `.gitignore` que las excluye.

## Verificación

Antes de dar por terminado un cambio en material Quarto:
1. `uv run quarto render <proyecto>` sin errores (revisar la salida: un error de Python detiene el render).
2. Comprobar en el HTML generado que figuras/elementos esperados existen (p. ej. `grep 'id="fig-…"'`).
3. Borrar las salidas generadas si no se van a publicar.
4. Si algo no se pudo verificar (p. ej. interactividad en navegador), decirlo explícitamente.

## Git

- Rama principal: `main`. No hacer commit ni push salvo que el usuario lo pida.
- No publicar (`quarto publish`, GitHub Pages) sin confirmación explícita del usuario.
