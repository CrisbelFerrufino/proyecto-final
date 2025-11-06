# graficos.py
import os
from data import get_tables_as_numpy
import matplotlib.pyplot as plt

os.makedirs("imagenes", exist_ok=True)

tables = get_tables_as_numpy()

md_lines = ["# Informe de gráficos\n",
            "Este archivo incluye las imágenes de posición y velocidad para cada una de las 6 tablas.\n"]

for name, d in tables.items():
    t = d["t"]
    x = d["x"]
    v = d["v"]
    mass = d["mass"]

    # Nombres de archivo seguros
    safe = name.replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_")
    fpos = f"imagenes/{safe}_pos.png"
    fvel = f"imagenes/{safe}_vel.png"

    # Gráfica posición vs tiempo
    plt.figure()
    plt.plot(t, x, marker='o')
    plt.title(f"{name} - Posición vs Tiempo")
    plt.xlabel("t [s]")
    plt.ylabel("x [m]")
    plt.grid()
    plt.savefig(fpos)
    plt.close()

    # Gráfica velocidad vs tiempo
    plt.figure()
    plt.plot(t, v, marker='o')
    plt.title(f"{name} - Velocidad vs Tiempo")
    plt.xlabel("t [s]")
    plt.ylabel("v [m/s]")
    plt.grid()
    plt.savefig(fvel)
    plt.close()

    # Descripción automática simple
    amp_x = (x.max() - x.min())/2
    mean_x = x.mean()
    max_v = v.max()
    min_v = v.min()

    md_lines.append(f"## {name}\n")
    md_lines.append(f"**Masa usada:** {mass:.3f} kg (factor en título * m_base)\n\n")
    md_lines.append(f"![Posición]({fpos})\n\n")
    md_lines.append(f"![Velocidad]({fvel})\n\n")
    md_lines.append("- Amplitud aproximada (x): {:.3f} m\n".format(amp_x))
    md_lines.append("- Valor medio de x: {:.3f} m\n".format(mean_x))
    md_lines.append(f"- Velocidad máxima: {max_v:.3f} m/s, mínima: {min_v:.3f} m/s\n\n")
    md_lines.append("---\n\n")

# Guardar informe
with open("informe_graficos.md", "w", encoding="utf-8") as f:
    f.writelines([line if line.endswith("\n") else line + "\n" for line in md_lines])

print("Se generaron imágenes en la carpeta 'imagenes' y se creó informe_graficos.md")
