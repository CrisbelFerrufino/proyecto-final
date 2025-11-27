from src.errores_coeficientes import errores_m_b
import numpy as np

def test_errores():
    error_m, error_b = errores_m_b(S=10, Sx=5, Sxx=20, Delta=100)
    assert np.isclose(error_m, np.sqrt(10/100))
    assert np.isclose(error_b, np.sqrt(20/100))
