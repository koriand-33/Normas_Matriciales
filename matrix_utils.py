import numpy as np

def norma_1(A):
    return np.linalg.norm(A, 1)

def norma_infinita(A):
    return np.linalg.norm(A, np.inf)

def norma_frobenius(A):
    return np.linalg.norm(A, 'fro')

def norma_2(A):
    return np.linalg.norm(A, 2)

def valores_propios(A):
    return np.linalg.eigvals(A)

def descomposicion_svd(A):
    return np.linalg.svd(A)

def sensibilidad_por_perturbacion(A, perturbacion=1e-3):
    A_pert = A + perturbacion * np.random.randn(*A.shape)
    delta = np.linalg.norm(A_pert - A, 'fro')
    cambio_norma = abs(norma_2(A_pert) - norma_2(A))
    return delta, cambio_norma