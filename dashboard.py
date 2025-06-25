import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from matrix_utils import (
    norma_1, norma_frobenius, norma_2,
    sensibilidad_por_perturbacion
)

# Configuración inicial de la app
st.set_page_config(page_title="Analizador de Normas Matriciales", layout="centered")
st.title("✩ Analizador de Normas Matriciales ✩")

# --- Ingreso dinámico de matriz ---
st.sidebar.header("Agregar filas o columnas")

if "filas" not in st.session_state:
    st.session_state.filas = 2
if "columnas" not in st.session_state:
    st.session_state.columnas = 3

col1, col2 = st.sidebar.columns(2)
if col1.button("➕ Agregar columna"):
    st.session_state.columnas += 1
if col2.button("➖ Quitar columna") and st.session_state.columnas > 1:
    st.session_state.columnas -= 1

col3, col4 = st.sidebar.columns(2)
if col3.button("➕ Agregar fila"):
    st.session_state.filas += 1
if col4.button("➖ Quitar fila") and st.session_state.filas > 1:
    st.session_state.filas -= 1

if "df_valores" not in st.session_state:
    st.session_state.df_valores = pd.DataFrame(
        np.zeros((st.session_state.filas, st.session_state.columnas)),
        columns=[f"C{j+1}" for j in range(st.session_state.columnas)]
    )
else:
    df_prev = st.session_state.df_valores
    filas_actual = st.session_state.filas
    columnas_actual = st.session_state.columnas

    if df_prev.shape[0] < filas_actual:
        filas_nuevas = pd.DataFrame(
            np.zeros((filas_actual - df_prev.shape[0], df_prev.shape[1])),
            columns=df_prev.columns
        )
        df_prev = pd.concat([df_prev, filas_nuevas], ignore_index=True)
    elif df_prev.shape[0] > filas_actual:
        df_prev = df_prev.iloc[:filas_actual, :]

    if df_prev.shape[1] < columnas_actual:
        cols_nuevas = [f"C{j+1}" for j in range(df_prev.shape[1], columnas_actual)]
        for c in cols_nuevas:
            df_prev[c] = 0.0
    elif df_prev.shape[1] > columnas_actual:
        df_prev = df_prev.iloc[:, :columnas_actual]

    st.session_state.df_valores = df_prev

st.subheader(" Ingresa los valores de la matriz directamente")
df_editado = st.data_editor(
    st.session_state.df_valores,
    num_rows="dynamic",
    use_container_width=True
)

st.session_state.df_valores = df_editado

A = df_editado.to_numpy()

# ──────────────────────────────
# 🔢 Visualizar matriz
# ──────────────────────────────
st.subheader(" Matriz ingresada")
st.dataframe(df_editado.style.format("{:.1f}"), use_container_width=True)


normas = {
    'Norma L1 (máx suma columnas)': norma_1(A),
    'Norma Frobenius (cuadrática)': norma_frobenius(A),
    'Norma L2 / Espectral (σ máx)': norma_2(A),
}

st.subheader("📋 Normas calculadas")
df_normas = pd.DataFrame({
    "Tipo de norma": list(normas.keys()),
    "Valor": list(normas.values())
})
st.table(df_normas.style.format({"Valor": "{:.4f}"}))

st.subheader("📊 Comparación gráfica")
fig, ax = plt.subplots(figsize=(7, 4))
colores = ['#1f77b4', '#2ca02c', '#d62728']
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


# Calcular sensibilidad
delta, cambio = sensibilidad_por_perturbacion(A)
sensibilidad_relativa = cambio / delta if delta != 0 else 0

if sensibilidad_relativa > 1:
    conclusion = "⚠️ La matriz muestra **alta sensibilidad numérica** ante perturbaciones. Esto podría indicar mal condicionamiento."
elif sensibilidad_relativa > 0.5:
    conclusion = "🔶 La matriz presenta **moderada sensibilidad**, es importante revisar estabilidad si se usa en contextos numéricos críticos."
elif sensibilidad_relativa > 0.2:
    conclusion = "✅ La matriz es **razonablemente estable** frente a perturbaciones pequeñas."
else:
    conclusion = "🟢 La matriz es **muy estable numéricamente**."

# Mostrar conclusiones (ya no hay comparación con norma ∞)
st.markdown(f"""
### Análisis obtenido:
{conclusion}
""")
