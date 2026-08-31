Tipos de datos en Python

Python tiene varios tipos de datos incorporados, organizados en las siguientes categorías:

# Tipos numéricos
* int — números enteros: 5, -10, 1000
* float — números decimales: 3.14, -0.5
* complex — números complejos: 3 + 4j

### Tipo de texto
*str — cadenas de texto: "Hola mundo", 'Python'

### Tipo booleano
* bool — valores lógicos: True o False

### Tipos de secuencia
* list — lista modificable: [1, 2, 3]
* tuple — tupla inmutable: (1, 2, 3)
* range — secuencia de números: range(0, 10)

### Tipos de mapeo
* dict — diccionario clave-valor: {"nombre": "Ana", "edad": 30}

### Tipos de conjunto
* set — conjunto no ordenado sin duplicados: {1, 2, 3}
* frozenset — versión inmutable de set

### Tipo binario
* bytes — secuencia de bytes inmutable: b"hola"
* bytearray — secuencia de bytes modificable
* memoryview — vista de memoria de otro objeto binario

### Tipo nulo
* NoneType — representa la ausencia de valor: None

## Ejemplo práctico
python
entero = 10
decimal = 3.14
texto = "Python"
booleano = True
lista = [1, 2, 3]
tupla = (1, 2, 3)
diccionario = {"clave": "valor"}
conjunto = {1, 2, 3}
nulo = None

print(type(entero))       # <class 'int'>
print(type(texto))        # <class 'str'>
print(type(lista))        # <class 'list'>

Podés usar la función type() para verificar el tipo de cualquier variable, y isinstance() para comprobar si un objeto pertenece a un tipo específico.
