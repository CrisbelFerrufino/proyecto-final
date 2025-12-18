import numpy as np

def linearizar(x, v):
    """
    Recibe: x (m), v (m/s)
    Devuelve: X = x^2, Y = v^2
    """
    X = x ** 2
    Y = v ** 2
    return X, Y
