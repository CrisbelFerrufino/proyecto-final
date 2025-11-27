import numpy as np

# 1. obtener omega
def obtener_omega(m, error_m):
    omega = np.sqrt(-m)
    error_omega = error_m / (2 * np.sqrt(-m))
    return omega, error_omega

# 2. calcular k por tabla
def calcular_k(masa, m, error_m):
    k = masa * (-m)
    error_k = masa * error_m
    return k, error_k

# 3. promedio ponderado
def promedio_ponderado(valores, errores):
    w = 1 / (errores**2)
    k_prom = np.sum(valores * w) / np.sum(w)
    error_k_prom = np.sqrt(1 / np.sum(w))
    return k_prom, error_k_prom

# 4. periodo para masa 9m
def calcular_periodo(k, error_k, masa_9m):
    T = 2 * np.pi * np.sqrt(masa_9m / k)
    error_T = T * 0.5 * (error_k / k)
    return T, error_T
