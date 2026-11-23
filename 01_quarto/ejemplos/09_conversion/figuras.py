"""Módulo normal de Python (sin celdas) que se importa desde un .qmd."""
import matplotlib.pyplot as plt


def grafica_cuadrados(n=10):
    xs = list(range(1, n + 1))
    plt.bar(xs, [x**2 for x in xs], color="seagreen")
    plt.xlabel("x")
    plt.ylabel("x²")
    plt.show()
