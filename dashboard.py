import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from matrix_utils import (
    norma_1, norma_infinita, norma_frobenius, norma_2,
    sensibilidad_por_perturbacion
)

# --- Datos base ---
A = np.array([[1, -2, 0], [4, -3, 4]])

# --- Cálculo de normas ---
normas = {
    'Norma L1 (máx suma columnas)': norma_1(A),
    'Norma ∞ (máx suma filas)': norma_infinita(A),
    'Norma Frobenius (cuadrática)': norma_frobenius(A),
    'Norma L2 / Espectral (σ máx)': norma_2(A),
}

# --- Análisis de sensibilidad ---
delta, cambio = sensibilidad_por_perturbacion(A)

# --- Streamlit layout ---
st.set_page_config(page_title="Analizador de Normas Matriciales", layout="centered")

st.title("📐 Analizador de Normas Matriciales")

# Matriz visual
st.subheader("🔢 Matriz de entrada")
df_matrix = pd.DataFrame(A)
st.dataframe(df_matrix.style.format("{:.1f}"), use_container_width=True)

# Normas como tabla
st.subheader("📋 Normas calculadas")
df_normas = pd.DataFrame({
    "Tipo de norma": list(normas.keys()),
    "Valor": list(normas.values())
})
st.table(df_normas.style.format({"Valor":"{:.4f}"}))

# Gráfico de comparación con puntos
st.subheader("📊 Comparación gráfica")
fig, ax = plt.subplots(figsize=(7, 4))
colores = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
nombres = list(normas.keys())
valores = list(normas.values())

for i, valor in enumerate(valores):
    ax.plot(i, valor, 'o', markersize=10, color=colores[i])
    ax.text(i, valor + 0.2, f'{valor:.4f}', ha='center', fontsize=9)

ax.set_xticks(range(len(nombres)))
ax.set_xticklabels(nombres, rotation=15)
ax.set_ylabel("Magnitud")
ax.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot(fig)

# Análisis de sensibilidad
st.subheader("🧪 Análisis de sensibilidad")
st.markdown(f"""
**Perturbación aplicada (Frobenius):** `{delta:.6f}`  
**Cambio en norma L2 (espectral):** `{cambio:.6f}`
""")

st.info("El análisis de sensibilidad muestra cómo una pequeña perturbación aleatoria afecta la norma L2. Una gran variación indica mayor inestabilidad numérica.")
