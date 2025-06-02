# Este programa solicita al usuario ingresar una lista de nombres 
# y luego mueve el nombre menor al inicio de la lista.

def leer_cantidad():
    while True:
        try:
            cantidad = int(input("¿Cuántos nombres va a ingresar?: "))
            if cantidad <= 0:
                print("Error. Debe ingresar un número mayor a 0.")
                continue
            return cantidad
        except ValueError:
            print("Error. Ingrese un número entero.")

def leer_nombres(cantidad):
    nombres = []
    for i in range(cantidad):
        nombre = input(f"Ingrese el nombre {i + 1}: ")
        nombres.append(nombre)
    return nombres

def mover_menor_al_inicio(nombres):
    if not nombres:
        return nombres

    menor = min(nombres)
    indice_menor = nombres.index(menor)
    nombres.pop(indice_menor)
    nombres.insert(0, menor)
    return nombres

if __name__ == "__main__":
    cantidad = leer_cantidad()
    nombres = leer_nombres(cantidad)
    nombres_modificados = mover_menor_al_inicio(nombres)
    print("Lista resultante:")
    print(nombres_modificados)
