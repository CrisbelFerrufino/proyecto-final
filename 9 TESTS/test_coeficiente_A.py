from coeficiente_A import coeficiente_A

def test_coef_A():
    x = [1, 2, 3]
    y = [2, 4, 6]  # A = 2
    assert abs(coeficiente_A(x, y) - 2) < 0.001
