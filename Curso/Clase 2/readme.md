# Programa saludador en Colab
```
print("Bienvenido a mi programa saludador")

nombre = input("Dime tu nombre y te saludo")

print(f"Bienvenido {nombre}")
```






# Cloude = 
```
Dame un ejemplo de codigo para copiar y pegar que muestre un grafico hecho con matplotlib para sorprender a mis estudiantes que te estan viendo con el poder de esta liberia

```

### Resultado =
```
import numpy as np
import matplotlib.pyplot as plt

# Creamos una grilla de puntos en el plano X-Y
x = np.linspace(-5, 5, 200)
y = np.linspace(-5, 5, 200)
X, Y = np.meshgrid(x, y)

# Función matemática que genera "ondas" concéntricas
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R) / (R + 0.1)  # +0.1 para evitar dividir por cero

# Creamos la figura en 3D
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Graficamos la superficie con un mapa de colores llamativo
surf = ax.plot_surface(X, Y, Z, cmap='plasma', edgecolor='none', antialiased=True)

# Agregamos una barra de color y título
fig.colorbar(surf, shrink=0.5, aspect=10, label='Altura (Z)')
ax.set_title('Ondas matemáticas en 3D', fontsize=16, fontweight='bold')
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')

# Ángulo de cámara para que se vea más impactante
ax.view_init(elev=30, azim=45)

plt.tight_layout()
plt.show()
```
# Resultado en colab
<img width="817" height="690" alt="image" src="https://github.com/user-attachments/assets/3d1cc140-fac5-45a1-b710-426cd1e82714" />




# Prueba en ChatGPT

```
Utiliza matplotlib para mostrarme un grafico de torta que muestre tasa de criminalidad de las 10 provincias con mayor tasa de argentina
```
* Resultado
<img width="768" height="794" alt="image" src="https://github.com/user-attachments/assets/c84752ed-1767-4c27-bfb6-81ad6e2517b3" />

* Codigo
  ```
  import matplotlib.pyplot as plt

# Fuente: SNIC 2024, Ministerio de Seguridad Nacional.
# Para hacer comparable la "criminalidad" entre jurisdicciones usamos
# la tasa de robos y tentativas de robo cada 100.000 habitantes.
datos = {
    "Córdoba": 1797.3,
    "San Juan": 1630.1,
    "Mendoza": 1511.2,
    "Neuquén": 1505.0,
    "Salta": 1391.6,
    "Santa Fe": 1250.0,
    "Santiago del Estero": 1276.6,
    "Río Negro": 967.2,
    "Catamarca": 926.4,
    "Jujuy": 755.8,
}

# Ordenar de mayor a menor
datos = dict(sorted(datos.items(), key=lambda x: x[1], reverse=True))

fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(
    datos.values(),
    labels=datos.keys(),
    autopct=lambda p: f"{p:.1f}%",
    startangle=90,
    pctdistance=0.72
)

ax.set_title(
    "Top 10 provincias argentinas por tasa de robos y tentativas de robo — 2024",
    fontsize=14,
    pad=18
)

ax.text(
    0.5, -0.08,
    "Tasa expresada como hechos cada 100.000 habitantes | SNIC 2024",
    transform=ax.transAxes,
    ha="center",
    fontsize=10
)

plt.tight_layout()
plt.show()
```
