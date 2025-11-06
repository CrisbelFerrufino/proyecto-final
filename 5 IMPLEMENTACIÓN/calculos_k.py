# calculos_k.py
import numpy as np
from data import get_tables_as_numpy

def detect_period_simple(t, x):
    # Detectar ceros ascendentes o máximos con comparación local
    # Estimar T como distancia entre máximos locales
    peaks = []
    for i in range(1, len(x)-1):
        if x[i] > x[i-1] and x[i] > x[i+1]:
            peaks.append(t[i])
        # Picos negativos (mínimos) se pueden usar, no obligatorio
    if len(peaks) < 2:
        # Usar cruces por cero para estimar T/2
        zeros = []
        for i in range(len(x)-1):
            if x[i] == 0 or (x[i] < 0 and x[i+1] > 0) or (x[i] > 0 and x[i+1] < 0):
                zeros.append(t[i])
        if len(zeros) >= 2:
            periods = np.diff(zeros) * 2  # porque cruces por cero ~ T/2
            return periods.mean() if len(periods)>0 else None
        return None
    periods = np.diff(peaks)
    return np.mean(periods) if len(periods)>0 else None

tables = get_tables_as_numpy()

te = 0.001  # s, error tiempo (consigna)
results = {}

for name, d in tables.items():
    t = d["t"]
    x = d["x"]
    mass = d["mass"]
    T = detect_period_simple(t, x)
    if T is None:
        print(f"[{name}] No se pudo estimar período con este método simple.")
        continue
    omega = 2 * np.pi / T
    k = mass * omega**2
    # incertidumbre simplificada: suponer sigma_T = te (conservador)
    sigma_T = te
    sigma_k = k * 2 * (sigma_T / T)
    results[name] = {"T": T, "sigma_T": sigma_T, "k": k, "sigma_k": sigma_k}
    print(f"{name}: T = {T:.4f} ± {sigma_T:.4f} s; k = {k:.3f} ± {sigma_k:.3f} N/m")

# Promedio de k (si hay varias)
ks = [v["k"] for v in results.values()]
errs = [v["sigma_k"] for v in results.values()]
if ks:
    k_mean = np.mean(ks)
    k_mean_err = np.sqrt(np.sum(np.array(errs)**2))/len(errs)
    print(f"\nConstante k promedio = {k_mean:.3f} ± {k_mean_err:.3f} N/m")
    # calcular periodo para masa 9m
    m_base = None
    # Recuperar m_base desde data (si user puso en data.py)
    try:
        from data import m_base
        m_base = m_base
    except:
        m_base = None
    if m_base:
        m9 = 9 * m_base
        T9 = 2 * np.pi * np.sqrt(m9 / k_mean)
        sigma_T9 = T9 * 0.5 * (k_mean_err / k_mean)
        print(f"Periodo estimado para masa 9m (m_base={m_base} kg): T9 = {T9:.4f} ± {sigma_T9:.4f} s")
    else:
        print("Para calcular T9, asegúrate de poner m_base (en kg) en data.py")
else:
    print("No hubo estimaciones de k.")
