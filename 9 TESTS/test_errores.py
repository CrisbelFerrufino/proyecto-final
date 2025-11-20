from errores_coeficientes import errores_coeficientes

def test_errores():
    x = [1, 2, 3]
    y = [2, 4, 6]
    A = 2
    B = 0
    error_A, error_B = errores_coeficientes(x, y, A, B)
    assert error_A >= 0
    assert error_B >= 0
