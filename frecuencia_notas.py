# Este programa solicita al usuario ingresar notas entre 1.0 y 7.0,
# Ademas, calcula la frecuencia de cada rango de notas y muestra un gráfico de barras.

def leer_notas():
    notas = []
    while True:
        try:
            cantidad = int(input("¿Cuántas notas va a ingresar?: "))
            if cantidad <= 0:
                print("Error. Ingrese una cantidad mayor a 0.")
                continue
            break
        except ValueError:
            print("Error. Ingrese un número entero.")

    for i in range(cantidad):
        while True:
            try:
                nota = float(input(f"Ingrese nota #{i + 1}: "))
                if 1.0 <= nota <= 7.0:
                    notas.append(nota)
                    break
                else:
                    print("Error. Debe estar entre 1.0 y 7.0.")
            except ValueError:
                print("Error. Ingrese un número válido.")
    return notas

def calcular_frecuencias(notas):
    categorias = {
        "1.0-1.9": 0,
        "2.0-2.9": 0,
        "3.0-3.9": 0,
        "4.0-4.9": 0,
        "5.0-5.9": 0,
        "6.0-7.0": 0,
    }

    for nota in notas:
        if 1.0 <= nota <= 1.9:
            categorias["1.0-1.9"] += 1
        elif 2.0 <= nota <= 2.9:
            categorias["2.0-2.9"] += 1
        elif 3.0 <= nota <= 3.9:
            categorias["3.0-3.9"] += 1
        elif 4.0 <= nota <= 4.9:
            categorias["4.0-4.9"] += 1
        elif 5.0 <= nota <= 5.9:
            categorias["5.0-5.9"] += 1
        elif 6.0 <= nota <= 7.0:
            categorias["6.0-7.0"] += 1

    return categorias

def mostrar_grafico(categorias):
    print("\nFrecuencia de notas:")
    for categoria, frecuencia in categorias.items():
        print(f"{categoria} | {'*' * frecuencia}")

if __name__ == "__main__":
    notas = leer_notas()
    frecuencias = calcular_frecuencias(notas)
    mostrar_grafico(frecuencias)
