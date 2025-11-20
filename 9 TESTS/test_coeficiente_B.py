from coeficiente_B import coeficiente_B

def test_coef_B():
    x = [1, 2, 3]
    y = [3, 4, 5]  # lineal: y = x + 2 → B = 2
    A = 1
    assert abs(coeficiente_B(x, y, A) - 2) < 0.001
