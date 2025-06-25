import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from matrix_utils import (
    norma_1, norma_infinita, norma_frobenius, norma_2,
    sensibilidad_por_perturbacion
)
from plot_utils import graficar_normas


import matplotlib.pyplot as plt

def graficar_normas_con_puntos(normas_dict):
    nombres = list(normas_dict.keys())
    valores = list(normas_dict.values())

    colores = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']  # azul, naranja, verde, rojo

    fig, ax = plt.subplots(figsize=(8, 5))

    # Crear el gráfico de puntos
    for i, (nombre, valor) in enumerate(zip(nombres, valores)):
        ax.plot(valor, i, 'o', markersize=12, color=colores[i], label=nombre)
        ax.text(valor + 0.1, i, f'{valor:.4f}', va='center', fontsize=10)

    ax.set_yticks(range(len(nombres)))
    ax.set_yticklabels(nombres, fontsize=12)
    ax.set_xlabel('Magnitud de la norma', fontsize=12)
    ax.set_title('Comparación de Normas Matriciales ', fontsize=14, fontweight='bold')
    ax.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    A = np.array([[1, -2, 0], [4, -3, 4]])  # Matriz
    
    print("══════════════════════════════════════════════")
    print("Matriz de entrada A:")
    print(A)
    print("══════════════════════════════════════════════")

    normas = {
        'Norma L1 (máx suma columnas)': norma_1(A),
        'Norma ∞ (máx suma filas)': norma_infinita(A),
        'Norma L2 / Espectral (σ máx)': norma_2(A),
        'Norma Frobenius': norma_frobenius(A),
    }

    print("\n Normas calculadas:")
    print("──────────────────────────────────────────────")
    for nombre, valor in normas.items():
        print(f"{nombre:<35}: {valor:>10.4f}")
    print("──────────────────────────────────────────────")

    graficar_normas_con_puntos(normas)
    

    delta, cambio = sensibilidad_por_perturbacion(A)
    print("\n Análisis de sensibilidad ante perturbación:")
    print(f"‣ Perturbación (norma Frobenius)      : {delta:.6f}")
    print(f"‣ Cambio en norma L2 (espectral)      : {cambio:.6f}")
    print("══════════════════════════════════════════════")
