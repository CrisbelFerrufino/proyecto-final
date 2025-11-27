
# Descripciones
## Gráfica del Movimiento Oscilatorio para Masa 9m

### 1. Objetivo
Representar gráficamente el movimiento oscilatorio del sistema masa–resorte considerando:

- La amplitud del movimiento.
- La frecuencia angular obtenida en el Punto 1.
- La ecuación del movimiento armónico simple.

---

### 2. Modelo Teórico

El movimiento de un oscilador armónico simple se describe mediante:

\[
x(t) = A\cos(\omega t)
\]

donde:

- \(A\) = amplitud,
- \(\omega\) = frecuencia angular,
- \(t\) = tiempo.

La amplitud puede derivarse del intercepto \(b\) del ajuste MMC:

\[
b = \omega^2 A^2
\]

\[
A = \frac{\sqrt{b}}{\omega}
\]

---

### 3. Gráfica del Movimiento

Para un tiempo de observación de 5 segundos:

- Se generan 500 puntos entre 0 y 5 s.
- Se evalúa la función \(x(t)\).
- Se presenta en un gráfico posición vs. tiempo.

---

### 4. Código Utilizado

```python
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
    plt.title(f"Oscilación para masa 9m (ω={omega:.3f})")
    plt.show()
