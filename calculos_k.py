# calculos_k.py
import numpy as np
from scipy.signal import find_peaks

# Si no tienes scipy instalado: poetry add scipy
# - OJO: si prefieres no instalar scipy, puedo darte otra versión que detecta picos "a mano".
# Datos de ejemplo (t y x) -> reemplaza / añade los conjuntos que tengas
datasets = {
    # "nombre": (t_array, x_array, masa_en_kg)
    # EJEMPLO: masa base m = 0.2 kg -> masares = 4*m = 0.8 kg
    "experimento_4m": (
        np.array([0.000, 0.200, 0.400, 0.600, 0.800, 1.000]),
        np.array([0.000, 0.951, 0.809, 0.588, 0.309, 0.000]),
        0.8  # aqui pones la masa en kg real: ejemplo 4*m si m=0.2 kg -> 0.8
    ),
    # Si tienes más tablas, agrégalas aquí con sus tiempos, posiciones y masa real
}

# Errores de medición (según consigna)
te = 0.001    # s
xe = 0.001    # m
ve = 0.001    # m/s  (no se usa directamente aquí)

def estimate_period_and_uncertainty(t, x):
    """
    Encuentra picos en x(t), calcula T medio y su incertidumbre.
    """
    # encontrar picos (mínimo parámetro de altura para evitar ruido)
    peaks_idx, _ = find_peaks(x, height=None, distance=2)
    if len(peaks_idx) < 2:
        # Si no hay picos detectables, intentar invertir la señal (cresta negativa)
        peaks_idx, _ = find_peaks(-x, height=None, distance=2)
    if len(peaks_idx) < 2:
        raise RuntimeError("No se detectaron suficientes picos para estimar el período.")

    peak_times = t[peaks_idx]
    periods = np.diff(peak_times)        # T entre picos consecutivos
    T_mean = np.mean(periods)
    # incertidumbre: combinación de la dispersión entre períodos y el error en tiempo te
    sigma_periods = np.std(periods, ddof=1) if len(periods) > 1 else 0.0
    sigma_T = np.sqrt(sigma_periods**2 + te**2)
    return T_mean, sigma_T, peak_times

def compute_k_from_T(mass, T, sigma_T):
    """
    k = m * (2π / T)^2
    Propagación: σ_k = k * 2 * (σ_T / T)
    """
    omega = 2 * np.pi / T
    k = mass * omega**2
    sigma_k = k * 2 * (sigma_T / T)
    return k, sigma_k

# Recolectar estimaciones de k
k_vals = []
k_errs = []

for name, (t, x, mass) in datasets.items():
    try:
        T, sigma_T, peaks = estimate_period_and_uncertainty(t, x)
    except RuntimeError as e:
        print(f"[{name}] Error: {e}")
        continue

    k, sigma_k = compute_k_from_T(mass, T, sigma_T)
    print(f"--- {name} ---")
    print(f"Periodos detectados (s) entre picos: {np.diff(peaks) if False else 'ver peak times abajo'}")
    print(f"Peak times: {peaks}")
    print(f"T = {T:.4f} ± {sigma_T:.4f} s")
    print(f"k = {k:.4f} ± {sigma_k:.4f} N/m (usando masa = {mass} kg)")
    print()

    k_vals.append(k)
    k_errs.append(sigma_k)

# Promediar k si hay varios experimentos
if len(k_vals) > 0:
    k_vals = np.array(k_vals)
    k_errs = np.array(k_errs)

    # Promedio con error típico (usamos promedio simple y error combinado)
    k_mean = np.mean(k_vals)
    # combinar incertidumbres (propagación simplificada: sqrt(sum(err_i^2))/N)
    k_mean_err = np.sqrt(np.sum(k_errs**2)) / len(k_errs)

    print(f"Constante k promedio = {k_mean:.4f} ± {k_mean_err:.4f} N/m")
else:
    print("No se pudo estimar k de ningún conjunto de datos.")

# Calcular periodo para masa 9m (si tienes una masa base: aquí uso primera masa / factor)
if len(datasets) > 0 and len(k_vals) > 0:
    # Tomo k_mean y calculo periodo para masa 9*m_base si sabes cuál es m_base:
    # Si tus masas en 'datasets' estaban en forma real (kg), necesitas la masa base m_base.
    # Aquí como ejemplo, si la primera entrada era "4m", y le pusiste masa=0.8 (=> m_base=0.2)
    # entonces:
    first_mass = list(datasets.values())[0][2]
    # intentar inferir m_base como first_mass / factor_estimated si conoces el factor. 
    # Para evitar suposiciones, pido usar directamente la masa 9*m_base:
    m_base = None  # <-- REEMPLAZA si conoces m_base en kg, por ejemplo m_base = 0.2

    if m_base is not None:
        m9 = 9 * m_base
        T9 = 2 * np.pi * np.sqrt(m9 / k_mean)
        # Propagación aproximada: σ_T9/T9 = 0.5 * σ_k/k_mean  (si masa exacta)
        sigma_T9 = T9 * 0.5 * (k_mean_err / k_mean)
        print()
        print(f"Periodo para masa 9m (m_base={m_base} kg): T9 = {T9:.4f} ± {sigma_T9:.4f} s")
    else:
        print()
        print("Para calcular el período de 9m necesito que me pongas el valor numérico de la masa base `m_base` (en kg).")
        print("Ejemplo: si la primera muestra era 4m y tú asignaste masa=0.8 kg, entonces m_base = 0.8/4 = 0.2 kg.")
