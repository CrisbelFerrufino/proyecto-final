# Descripciones 
## Cálculo de la Constante Elástica k y del Periodo de Oscilación para Masa 9m

### 1. Objetivo
Determinar los parámetros dinámicos principales del sistema masa–resorte:

- La constante elástica \(k\) a partir de la pendiente del ajuste lineal.
- La incertidumbre asociada \(\Delta k\).
- El periodo de oscilación \(T\) para una masa equivalente a \(9m\).
- Su incertidumbre \(\Delta T\).

---

### 2. Datos Experimentales
Los datos utilizados provienen del análisis de la Semana 4:

- Pendientes \(m_i\) de cada tabla experimental.
- Incertidumbres \(\Delta m_i\).
- Masa utilizada en cada prueba \(M_i\).

*(Los valores numéricos se colocarán aquí cuando se extraigan de los cálculos.)*

---

### 3. Cálculo de la Frecuencia Angular \(\omega\)
Del ajuste lineal:

\[
m = -\omega^2
\]

Por lo tanto:

\[
\omega = \sqrt{-m}
\]

Error asociado:

\[
\Delta\omega = \frac{\Delta m}{2\sqrt{-m}}
\]

---

### 4. Cálculo de la Constante Elástica k

Para cada tabla:

\[
k_i = M_i \cdot \omega_i^2 = M_i(-m_i)
\]

Error:

\[
\Delta k_i = M_i \Delta m_i
\]

---

### 5. Valor Representativo de k — Promedio Ponderado

\[
\bar{k} =
\frac{\sum k_i / (\Delta k_i)^2}
     {\sum 1 / (\Delta k_i)^2}
\]

\[
\Delta\bar{k} = 
\sqrt{\frac{1}{\sum 1 / (\Delta k_i)^2}}
\]

Este valor representa la constante elástica final determinada experimentalmente.

---

### 6. Periodo de Oscilación para Masa 9m

\[
M_{9m} = 9m
\]

\[
T = 2\pi \sqrt{\frac{M_{9m}}{\bar{k}}}
\]

Incertidumbre:

\[
\Delta T =
T \left(
\frac{1}{2}
\frac{\Delta\bar{k}}{\bar{k}}
\right)
\]

---

### 7. Código Utilizado

```python
import numpy as np

def obtener_omega(m, error_m):
    omega = np.sqrt(-m)
    error_omega = error_m / (2 * np.sqrt(-m))
    return omega, error_omega

def calcular_k(masa, m, error_m):
    k = masa * (-m)
    error_k = masa * error_m
    return k, error_k

def promedio_ponderado(valores, errores):
    w = 1 / (errores**2)
    k_prom = np.sum(valores * w) / np.sum(w)
    error_k_prom = np.sqrt(1 / np.sum(w))
    return k_prom, error_k_prom

def calcular_periodo(k, error_k, masa_9m):
    T = 2 * np.pi * np.sqrt(masa_9m / k)
    error_T = T * 0.5 * (error_k / k)
    return T, error_T
