import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Crear carpeta graficas si no existe
os.makedirs("../graficas", exist_ok=True)

def generar_grafica(archivo_csv, nombre_salida):
    data = pd.read_csv(archivo_csv)
    
    t = data["t"]
    x = data["x"]

    A, B = np.polyfit(t, x, 1)

    plt.figure()
    plt.scatter(t, x, label="Datos")
    t_linea = np.linspace(min(t), max(t), 100)
    plt.plot(t_linea, A*t_linea + B, label="Ajuste lineal")

    plt.xlabel("t (s)")
    plt.ylabel("x (m)")
    plt.title(f"Gráfica {nombre_salida}")
    plt.legend()
    plt.grid()

    ruta = f"../graficas/{nombre_salida}.png"
    plt.savefig(ruta, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"✔ Imagen generada: {ruta}")

# Generar todas
generar_grafica("tabla1.csv", "tabla1")
generar_grafica("tabla2.csv", "tabla2")
generar_grafica("tabla3.csv", "tabla3")
generar_grafica("tabla4.csv", "tabla4")
generar_grafica("tabla5.csv", "tabla5")
generar_grafica("tabla6.csv", "tabla6")
