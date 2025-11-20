import math

def linearizar(x, xmax):
    """
    Aplica la transformación Y = arccos(X / Xmax)
    x = posiciones X medidas
    xmax = valor máximo de X medido
    """
    y = [math.acos(xi / xmax) for xi in x]
    return y
