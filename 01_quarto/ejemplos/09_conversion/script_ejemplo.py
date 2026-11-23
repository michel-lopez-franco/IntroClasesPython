# %% [markdown]
# ---
# title: "Script de Python renderizado con Quarto"
# format: html
# jupyter: python3
# ---

# %% [markdown]
# Este es un archivo **.py normal** escrito en formato *percent*:
#
# - `# %%` inicia una celda de código.
# - `# %% [markdown]` inicia una celda de texto (cada línea empieza con `# `).
#
# Se puede ejecutar con `python script_ejemplo.py` **y** renderizar con Quarto.

# %%
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14159 * self.radio**2


# %% [markdown]
# ## Usando la clase

# %%
for r in [1, 2, 3]:
    c = Circulo(r)
    print(f"Radio {r}: área = {c.area():.2f}")
