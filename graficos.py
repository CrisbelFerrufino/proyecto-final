import pandas as pd
import matplotlib.pyplot as plt
import os

# Carpeta
os.makedirs("graficas", exist_ok=True)

# Lista archivos CSV
tablas = [
    ("tabla1.csv", "Masa 4m"),
    ("tabla2.csv", "Masa 3m"),
    ("tabla3.csv", "Masa 3m"),
    ("tabla4.csv", "Masa 2m"),
    ("tabla5.csv", "Masa 2m"),
    ("tabla6.csv", "Masa 1m")
]

for archivo, titulo in tablas:
    ruta = os.path.join("data", archivo)
    df = pd.read_csv(ruta)

    plt.figure()
    plt.plot(df["t"], df["x"])
    plt.xlabel("Tiempo t [s]")
    plt.ylabel("Posición x [m]")
    plt.title(f"Movimiento Armónico Simple - {titulo}")

    salida = os.path.join("graficas", f"grafica_{archivo.replace('.csv', '')}.png")
    plt.savefig(salida, dpi=300)
    plt.close()

print("Todas las gráficas fueron generadas correctamente.")
