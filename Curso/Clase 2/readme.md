#Programa saludador en Colab
```
print("Bienvenido a mi programa saludador")

nombre = input("Dime tu nombre y te saludo")

print(f"Bienvenido {nombre}")
```






#Cloude = 
```
Dame un ejemplo de codigo para copiar y pegar que muestre un grafico hecho con matplotlib para sorprender a mis estudiantes que te estan viendo con el poder de esta liberia

```

#Resultado =
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
