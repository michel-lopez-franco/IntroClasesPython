# 🐍 Introducción a Programación Orientada a Objetos en Python

Curso completo de Programación Orientada a Objetos (POO) en Python, diseñado para estudiantes de maestría en CUCEI.

## 📋 Descripción

Este repositorio contiene material didáctico completo para aprender los conceptos fundamentales y avanzados de la Programación Orientada a Objetos utilizando Python. El curso está estructurado en módulos progresivos que van desde los conceptos básicos hasta implementaciones avanzadas.

## 🎯 Objetivos del Curso

- Comprender los fundamentos de la Programación Orientada a Objetos
- Dominar la creación y uso de clases y objetos en Python
- Aplicar los cuatro pilares de la POO: Encapsulamiento, Herencia, Polimorfismo y Abstracción
- Implementar patrones de diseño comunes
- Desarrollar proyectos prácticos utilizando POO

## 📚 Contenido del Curso

### Módulo 1: Fundamentos

- **[01_Introduccion_Clases_Objetos.ipynb](01_Introduccion_Clases_Objetos.ipynb)**
  - ¿Qué es la POO?
  - Clases y objetos
  - Instanciación de objetos
  - Diferencia entre clase e instancia

### Módulo 2: Componentes Básicos

- **[02_Atributos_Metodos.ipynb](02_Atributos_Metodos.ipynb)**

  - Atributos de instancia y de clase
  - Métodos de instancia
  - Métodos de clase
  - Métodos estáticos

- **[03_Constructor_Self.ipynb](03_Constructor_Self.ipynb)**
  - El método `__init__`
  - El parámetro `self`
  - Inicialización de objetos
  - Valores por defecto

### Módulo 3: Pilares de la POO

- **[04_Herencia.ipynb](04_Herencia.ipynb)**

  - Herencia simple y múltiple
  - Método `super()`
  - Sobrescritura de métodos
  - MRO (Method Resolution Order)

- **[05_Encapsulamiento_Propiedades.ipynb](05_Encapsulamiento_Propiedades.ipynb)**

  - Modificadores de acceso
  - Atributos privados y protegidos
  - Properties (@property)
  - Getters y Setters

- **[06_Polimorfismo.ipynb](06_Polimorfismo.ipynb)**
  - Polimorfismo de métodos
  - Duck typing
  - Interfaces informales
  - Sobrecarga de operadores

### Módulo 4: Conceptos Avanzados

- **[07_Metodos_Especiales.ipynb](07_Metodos_Especiales.ipynb)**

  - Métodos mágicos (dunder methods)
  - `__str__` y `__repr__`
  - `__len__`, `__getitem__`, `__setitem__`
  - Operadores aritméticos y de comparación

- **[08_Composicion_Agregacion.ipynb](08_Composicion_Agregacion.ipynb)**

  - Composición vs Herencia
  - Agregación
  - Relaciones entre objetos
  - Ventajas de la composición

- **[09_Clases_Abstractas.ipynb](09_Clases_Abstractas.ipynb)**
  - ABC (Abstract Base Classes)
  - Métodos abstractos
  - Interfaces en Python
  - Patrones de diseño

### Módulo 5: Proyecto Integrador

- **[10_Proyecto_Integrador.ipynb](10_Proyecto_Integrador.ipynb)**
  - Aplicación práctica de todos los conceptos
  - Diseño de un sistema completo
  - Buenas prácticas
  - Documentación y testing

## 🛠️ Requisitos Previos

- Python 3.8 o superior
- Jupyter Notebook o JupyterLab
- Conocimientos básicos de programación en Python
- Familiaridad con estructuras de datos básicas

## 📦 Instalación

1. Clona este repositorio:

```bash
git clone <url-del-repositorio>
cd IntroClasesPython
```

2. Crea un entorno virtual (recomendado):

```bash
python -m venv venv
source venv/bin/activate  # En macOS/Linux
```

3. Instala las dependencias:

```bash
pip install jupyter notebook numpy pandas
```

4. Inicia Jupyter Notebook:

```bash
jupyter notebook
```

## 🚀 Cómo Usar Este Curso

1. **Orden Recomendado**: Sigue los notebooks en orden numérico (01 al 10)
2. **Práctica Activa**: Ejecuta cada celda de código y experimenta con variaciones
3. **Ejercicios**: Completa los ejercicios propuestos al final de cada notebook
4. **Proyecto**: Dedica tiempo suficiente al proyecto integrador (notebook 10)

## 📝 Estructura de Cada Notebook

Cada notebook incluye:

- 📖 Explicación teórica del concepto
- 💻 Ejemplos de código comentados
- ✏️ Ejercicios prácticos
- 🔍 Casos de uso reales
- ❓ Preguntas de revisión

## 🎓 Evaluación

El curso se evalúa mediante:

- Comprensión de conceptos teóricos (30%)
- Ejercicios prácticos en cada módulo (30%)
- Proyecto integrador final (40%)

## 📖 Recursos Adicionales

### Documentación Oficial

- [Python Documentation - Classes](https://docs.python.org/3/tutorial/classes.html)
- [Python Data Model](https://docs.python.org/3/reference/datamodel.html)

### Libros Recomendados

- "Python Object-Oriented Programming" - Dusty Phillips
- "Fluent Python" - Luciano Ramalho
- "Clean Code" - Robert C. Martin

### Tutoriales en Línea

- [Real Python - OOP](https://realpython.com/python3-object-oriented-programming/)
- [Python OOP Tutorial](https://www.programiz.com/python-programming/object-oriented-programming)

## 🤝 Contribuciones

Este es un proyecto educativo. Si encuentras errores o tienes sugerencias:

1. Abre un Issue describiendo el problema o mejora
2. Si deseas contribuir código, crea un Pull Request

## 📧 Contacto

Para preguntas sobre el curso:

- Instructor: [Tu nombre]
- Email: [Tu email]
- Horario de consulta: [Días y horarios]

## 📄 Licencia

Este material está diseñado con fines educativos para el programa de maestría en CUCEI.

## 🗓️ Actualizaciones

- **Última actualización**: Diciembre 2025
- **Versión de Python**: 3.8+
- **Estado**: Activo

---

**¡Feliz aprendizaje! 🎉**

> "La programación orientada a objetos nos permite organizar el código de manera que refleje mejor el mundo real, haciendo nuestras soluciones más intuitivas y mantenibles."

---

### 📌 Notas Importantes

- Asegúrate de tener tu entorno de Python configurado antes de comenzar
- Practica cada concepto antes de avanzar al siguiente módulo
- No dudes en experimentar y modificar los ejemplos
- La mejor forma de aprender POO es escribiendo código

### 🔧 Solución de Problemas Comunes

**Problema**: Jupyter Notebook no inicia

```bash
pip install --upgrade jupyter
```

**Problema**: Módulos no encontrados

```bash
pip install -r requirements.txt
```

**Problema**: Errores de sintaxis

- Verifica que estés usando Python 3.8 o superior
- Revisa la indentación de tu código

---

**Desarrollado para el programa de Maestría - CUCEI**
