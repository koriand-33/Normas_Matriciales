#  Normas Matriciales

Este repositorio contiene una herramienta interactiva para el análisis y visualización de normas matriciales, implementada con Python y Streamlit. El objetivo es facilitar la comprensión de diferentes normas aplicadas a matrices y cómo estas responden ante perturbaciones.

## Contenido

- Cálculo de distintas normas matriciales:
  - Norma 1 (||·||₁)
  - Norma infinita (||·||∞)
  - Norma de Frobenius
  - Norma 2 (espectral)
- Análisis de sensibilidad por perturbación
- Visualización con gráficos
- Dashboard en Streamlit para uso interactivo

## ¿Qué son las normas matriciales?

Las normas matriciales permiten medir el "tamaño" o "magnitud" de una matriz. Son herramientas fundamentales en análisis numérico, estabilidad de algoritmos y control de errores en operaciones matriciales.

Este proyecto presenta visualmente cómo se comportan las distintas normas y cómo responden ante pequeñas perturbaciones aleatorias en la matriz.

##  Cómo usar:

1. Clona el repositorio:
   ```bash
   git clone https://github.com/koriand-33/Normas_Matriciales.git
   cd Normas_Matriciales

2. Instala los requerimientos
   ```bash
   pip install -r requirements.txt

3. Ejecuta la app de Stremlit:
   ```bash
   streamlit run app.py

## Opción en terminal sin descargar Streamlit: ##

   ```bash
   python main.py
