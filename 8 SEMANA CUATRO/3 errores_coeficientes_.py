import math

def errores_coeficientes(x, y, A, B):
    """
    Calcula los errores estándar de A y B en el ajuste lineal.
    """
    N = len(x)
    sum_x = sum(x)

    # Calcular residuos
    residuos = [(y[i] - (A * x[i] + B))**2 for i in range(N)]
    sigma2 = sum(residuos) / (N - 2)

    sum_x2 = sum([xi**2 for xi in x])
    delta = N * sum_x2 - (sum_x ** 2)

    error_A = math.sqrt(N * sigma2 / delta)
    error_B = math.sqrt(sum_x2 * sigma2 / delta)

    return error_A, error_B
