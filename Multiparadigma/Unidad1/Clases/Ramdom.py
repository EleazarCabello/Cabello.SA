import random

# Generar un número decimal aleatorio entre 1.0 y 10.0 con precisión de dos decimales
numero_decimal = round(random.uniform(1.0, 10.0), 2)
print(numero_decimal)

import random

opciones = ['manzana', 'banana', 'cereza', 'uva']

elemento_aleatorio = random.choice(opciones)
print(elemento_aleatorio)

import random

# Generar un número decimal aleatorio entre 0 y 1
numero_decimal = random.random()
print(numero_decimal)

import random

# Generar un número aleatorio entre 1 y 100
numero_aleatorio = random.randint(1, 100)
print(numero_aleatorio)

import random

cartas = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
random.shuffle(cartas)
print(cartas)