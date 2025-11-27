import numpy as np

def ajuste_mmc(X, Y):

    n = len(X)

    S = n
    Sx = np.sum(X)
    Sy = np.sum(Y)
    Sxx = np.sum(X * X)
    Sxy = np.sum(X * Y)

    Delta = S * Sxx - Sx**2

    m = (S * Sxy - Sx * Sy) / Delta
    b = (Sxx * Sy - Sx * Sxy) / Delta

    return m, b, S, Sx, Sxx, Delta
