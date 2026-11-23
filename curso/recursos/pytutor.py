"""Incrusta una visualización de Python Tutor (https://pythontutor.com) en un capítulo.

Uso en un .qmd (celda oculta):

    ```{python}
    #| echo: false
    from recursos.pytutor import pytutor
    pytutor('''
    class Perro:
        pass
    p = Perro()
    ''')
    ```
"""
import html
import textwrap
from urllib.parse import quote

from IPython.display import HTML

_BASE = "https://pythontutor.com"


def _parametros(codigo: str, paso: int) -> str:
    return (
        f"code={quote(codigo, safe='')}"
        f"&cumulative=false&curInstr={paso}&heapPrimitives=nevernest"
        "&mode=display&origin=opt-frontend.js&py=311"
        "&rawInputLstJSON=%5B%5D&textReferences=false"
    )


def pytutor(codigo: str, altura: int = 760, paso: int = 0) -> HTML:
    """Devuelve el iframe de Python Tutor para `codigo`.

    altura: alto del iframe en píxeles. Con el ancho de la columna del libro, Python Tutor
            dibuja marcos y objetos DEBAJO del código, así que necesita bastante altura.
    paso:   paso de ejecución que se muestra al cargar (0 = el inicio).
    """
    codigo = textwrap.dedent(codigo).strip("\n") + "\n"
    params = _parametros(codigo, paso)
    embed = f"{_BASE}/iframe-embed.html#{params}"
    enlace = f"{_BASE}/visualize.html#{params}"
    return HTML(
        f'<div class="pytutor">'
        f'<iframe src="{html.escape(embed)}" width="100%" height="{altura}" loading="lazy" '
        f'style="border:1px solid rgba(128,128,128,.35); border-radius:8px; background:white; resize:vertical; overflow:auto" '
        f'title="Visualización paso a paso en Python Tutor"></iframe>'
        f'<p class="small text-muted mb-0">Usa <b>Next &gt;</b> y <b>&lt; Prev</b> para avanzar '
        f'paso a paso (puedes estirar el recuadro desde su esquina inferior). <a href="{html.escape(enlace)}" target="_blank" rel="noopener">'
        f'Abrir en Python Tutor ↗</a></p></div>'
    )
