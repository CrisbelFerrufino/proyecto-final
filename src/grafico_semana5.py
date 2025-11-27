import numpy as np
import matplotlib.pyplot as plt

def graficar_movimiento(A, omega, tiempo=5):
    t = np.linspace(0, tiempo, 500)
    x = A * np.cos(omega * t)

    plt.figure(figsize=(8,4))
    plt.plot(t, x)
    plt.grid()
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Posición (m)")
    plt.title(f"Oscilación masa 9m (ω={omega:.3f})")
    plt.show()
