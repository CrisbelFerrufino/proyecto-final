from coeficiente_A import coeficiente_A
from coeficiente_B import coeficiente_B
from errores_coeficientes import errores_coeficientes

def ajuste_mmc(t, y):
    """
    Ajuste completo:
    calcula A, B y sus errores
    """
    A = coeficiente_A(t, y)
    B = coeficiente_B(t, y, A)
    error_A, error_B = errores_coeficientes(t, y, A, B)

    return A, B, error_A, error_B
