import matplotlib.pyplot as plt

# Datos del movimiento
t = [0.000, 0.200, 0.400, 0.600, 0.800, 1.000]
x = [0.000, 0.951, 0.809, 0.588, 0.309, 0.000]
v = [0.000, -0.485, -0.923, -1.271, -1.494, -1.571]

# Gráfico posición vs tiempo
plt.plot(t, x, marker='o')
plt.title("Posición vs Tiempo (MAS)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Posición (m)")
plt.grid()
plt.savefig("grafico_posicion.png")
plt.close()

# Gráfico velocidad vs tiempo
plt.plot(t, v, marker='o', color='red')
plt.title("Velocidad vs Tiempo (MAS)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Velocidad (m/s)")
plt.grid()
plt.savefig("grafico_velocidad.png")
plt.close()

print("Listo. Gráficos guardados.")
