### Prop en Chatgpt
```
Quiero un programa en python que cree un vector de un millon de elementos con valores aleatorios entre 1 y 10. Luego que lo recorra y a cada elemento le sume 10. Quiero que tomes el tiempo que tarda en recorrer el array y a cada elemento sumarle 10.
```


### Resultado del promp

```
import random
import time

# Crear un vector de 1.000.000 de elementos
vector = [random.randint(1, 10) for _ in range(1_000_000)]

# Comenzar a medir el tiempo
inicio = time.perf_counter()

# Recorrer el vector y sumar 10 a cada elemento
for i in range(len(vector)):
    vector[i] += 10

# Finalizar medición
fin = time.perf_counter()

# Mostrar resultado
tiempo = fin - inicio

print(f"Tiempo de procesamiento: {tiempo:.6f} segundos")
print(f"Primeros 10 elementos: {vector[:10]}")

```
