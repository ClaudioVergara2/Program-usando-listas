# Este programa calcula la media, desviación estándar y moda de una lista de números enteros.

import math
from collections import Counter

def calcular_media(lista):
    return sum(lista) / len(lista)

def calcular_desviacion_estandar(lista):
    media = calcular_media(lista)
    varianza = sum((x - media) ** 2 for x in lista) / len(lista)
    return math.sqrt(varianza)

def calcular_moda(lista):
    frecuencias = Counter(lista)
    max_frecuencia = max(frecuencias.values())
    modas = [num for num, freq in frecuencias.items() if freq == max_frecuencia]
    return min(modas)

input("Este programa calcula la media, desviación estándar y moda de una lista de números enteros.\n"
      "Presiona Enter para continuar...")

while True:
    entrada = input("Ingrese los valores separados por coma:")
    try:
        valores = list(map(int, entrada.split(',')))
        n = valores[0]
        numeros = valores[1:]

        if not (1 < n <= 100):
            print("Error: n debe estar en el rango 2 a 100.\n")
            continue
        if len(numeros) != n:
            print("Error: la cantidad de números no coincide con n.\n")
            continue

        media = calcular_media(numeros)
        desviacion = calcular_desviacion_estandar(numeros)
        moda = calcular_moda(numeros)

        print(f"{media:.2f}, {desviacion:.2f}, {moda}")
        break

    except ValueError:
        print("Error: entrada inválida. Asegúrate de ingresar solo números enteros separados por comas.\n")
