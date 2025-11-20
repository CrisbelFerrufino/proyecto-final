def coeficiente_A(x, y):
    """
    Calcula el coeficiente A usando la fórmula de mínimos cuadrados.
    x = tiempos t
    y = arccos(X / Xmax)
    """

    N = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum([x[i] * y[i] for i in range(N)])
    sum_x2 = sum([x[i]**2 for i in range(N)])

    A = (N * sum_xy - sum_x * sum_y) / (N * sum_x2 - (sum_x ** 2))
    return A
