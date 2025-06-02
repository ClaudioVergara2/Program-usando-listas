# Este programa crea una lista de nombres y los ordena alfabéticamente.

def leer_nombres():
    while True:
        try:
            cantidad = int(input("¿Cuántos nombres va a ingresar?: "))
            if cantidad <= 0:
                print("Error. Debe ingresar un número mayor a 0.")
                continue
            break
        except ValueError:
            print("Error. Ingrese un número entero.")

    nombres = []
    for i in range(cantidad):
        nombre = input(f"Ingrese el nombre {i + 1}: ")
        nombres.append(nombre)
    
    return nombres

def rotar_lista(nombres):
    if len(nombres) > 0:
        ultimo = nombres.pop()
        nombres.insert(0, ultimo)
    return nombres

nombres = leer_nombres()
nombres_rotados = rotar_lista(nombres)
print("Lista resultante:")
print(nombres_rotados)
