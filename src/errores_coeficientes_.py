import numpy as np

def errores_m_b(S, Sx, Sxx, Delta):
    error_m = np.sqrt(S / Delta)
    error_b = np.sqrt(Sxx / Delta)
    return error_m, error_b
