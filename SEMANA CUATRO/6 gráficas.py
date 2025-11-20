import matplotlib.pyplot as plt
import numpy as np

def graficar(t, y, A, B):
    """
    Grafica los datos linearizados y la recta de ajuste
    """
    plt.scatter(t, y, label="Datos linearizados")
    
    t_linea = np.linspace(min(t), max(t), 100)
    y_linea = A * t_linea + B

    plt.plot(t_linea, y_linea, label="Ajuste lineal", linewidth=2)
    plt.xlabel("t (s)")
    plt.ylabel("arccos(X/Xmax)")
    plt.title("Ajuste por Mínimos Cuadrados")
    plt.legend()
    plt.grid()
    plt.show()
