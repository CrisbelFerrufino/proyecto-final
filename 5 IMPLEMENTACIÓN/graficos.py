
import os
import matplotlib.pyplot as plt
from data import get_tables_as_numpy

# Crear la carpeta de imágenes 
if not os.path.exists("imagenes"):
    os.mkdir("imagenes")

# Obtener las tablas de datos desde data.py
tablas = get_tables_as_numpy()

# Lista donde se irá guardando el contenido 
informe = [
    "# Informe de Gráficos\n",
    "En esta sección se presentan las gráficas de posición y velocidad obtenidas para las seis tablas del experimento.\n",
    "Cada imagen fue generada automáticamente a partir de los datos registrados.\n\n"
]

# Generar  gráficas de las tablas
for nombre, datos in tablas.items():
    t = datos["t"]
    x = datos["x"]
    v = datos["v"]
    masa = datos["mass"]

    # Nombres de los archivos de imagen
    nombre_seguro = nombre.replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_")
    img_pos = f"imagenes/{nombre_seguro}_pos.png"
    img_vel = f"imagenes/{nombre_seguro}_vel.png"

    # --- Gráfica 1: Posición vs Tiempo ---
    plt.figure()
    plt.plot(t, x, marker='o', color='tab:blue')
    plt.title(f"{nombre} - Posición vs Tiempo")
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Posición [m]")
    plt.grid(True)
    plt.savefig(img_pos)
    plt.close()

    # --- Gráfica 2: Velocidad vs Tiempo ---
    plt.figure()
    plt.plot(t, v, marker='o', color='tab:orange')
    plt.title(f"{nombre} - Velocidad vs Tiempo")
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Velocidad [m/s]")
    plt.grid(True)
    plt.savefig(img_vel)
    plt.close()

    # Cálculos básicos para el informe
    amplitud = (x.max() - x.min()) / 2
    media_x = x.mean()
    v_max = v.max()
    v_min = v.min()

    # Agregar los resultados al informe Markdown
    informe.append(f"## {nombre}\n")
    informe.append(f"- Masa usada: **{masa:.3f} kg**\n")
    informe.append(f"- Amplitud aproximada: **{amplitud:.3f} m**\n")
    informe.append(f"- Valor medio de posición: **{media_x:.3f} m**\n")
    informe.append(f"- Velocidad máxima: **{v_max:.3f} m/s**\n")
    informe.append(f"- Velocidad mínima: **{v_min:.3f} m/s**\n\n")
    informe.append(f"![Gráfico de posición]({img_pos})\n\n")
    informe.append(f"![Gráfico de velocidad]({img_vel})\n\n")
    informe.append("---\n\n")

# Guardar el contenido
with open("informe_graficos.md", "w", encoding="utf-8") as archivo:
    archivo.writelines(informe)

print("Se generaron las 6 gráficas y se creó el archivo 'informe_graficos.md'.")
