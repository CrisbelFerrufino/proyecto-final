def coeficiente_B(x, y, A):
    """
    Calcula el coeficiente B usando fórmula de mínimos cuadrados
    """
    N = len(x)
    sum_x = sum(x)
    sum_y = sum(y)

    B = (sum_y - A * sum_x) / N
    return B
