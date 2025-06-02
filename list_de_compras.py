# Programa para ordenar alfabéticamente la lista de compras

def obtener_lista_productos():
    while True:
        try:
            n = int(input("Ingrese la cantidad de productos: "))
            if 1 < n < 100:
                break
            else:
                print("Error: El número debe estar entre 2 y 99.")
        except ValueError:
            print("Error: Ingrese un número entero válido.")
    
    productos = []
    print("Ingrese los productos uno por uno:")
    while len(productos) < n:
        producto = input(f"- ").strip()
        if not producto:
            print("El producto no puede estar vacío.")
        elif producto.isdigit():
            print("Error: No se permiten números como productos.")
        else:
            productos.append(producto)
    return productos

def main():
    productos = obtener_lista_productos()
    productos.sort()
    print("\nLista ordenada alfabéticamente:")
    for producto in productos:
        print(producto)

if __name__ == "__main__":
    main()
