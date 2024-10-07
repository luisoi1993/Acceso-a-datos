def mostrar_productos(productos):
    if not productos:
        print("No hay productos disponibles en la tienda.")
    else:
        print("\nLista de productos disponibles:")
        for producto in productos:
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Cantidad: {producto[2]}, Precio: {producto[3]:.2f} €")
    print("\n")

def agregar_producto(productos, historial):
    if len(productos) >= 8:
        print("Error: No se pueden añadir más de 8 productos en la tienda.")
        return

    id_producto = input("Introduce el ID del producto: ")
    nombre = input("Introduce el nombre del producto: ")
    cantidad = int(input("Introduce la cantidad del producto: "))
    precio = float(input("Introduce el precio del producto: "))

    if cantidad < 0 or precio < 0:
        print("La cantidad y el precio deben ser valores positivos.")
        return

    for producto in productos:
        if producto[0] == id_producto:
            producto[2] += cantidad  # Actualiza la cantidad
            producto[3] = precio  # Actualiza el precio
            print(f"Producto '{nombre}' actualizado en la tienda.")
            return

    # Si el producto no existe, se agrega
    productos.append([id_producto, nombre, cantidad, precio])
    historial.append([id_producto, nombre, [precio]])  # Agregar a historial
    print(f"Producto '{nombre}' añadido a la tienda.")

def eliminar_producto(productos, historial):
    nombre = input("Introduce el nombre del producto a eliminar: ")
    for producto in productos:
        if producto[1] == nombre:
            historial_item = next((h for h in historial if h[0] == producto[0]), None)
            if historial_item:
                historial_item[2].append(producto[3])  # Añadir el precio al historial
            productos.remove(producto)
            print(f"Producto '{nombre}' eliminado de la tienda.")
            return
    print(f"El producto '{nombre}' no se encuentra en la tienda.")

def comprar_producto(productos, carrito):
    nombre = input("Introduce el nombre del producto que deseas comprar: ")
    cantidad = int(input("Introduce la cantidad que deseas comprar: "))

    for producto in productos:
        if producto[1] == nombre:
            if producto[2] >= cantidad:
                producto[2] -= cantidad  # Actualiza el inventario
                carrito.append([producto[1], cantidad, producto[3]])  # Agrega al carrito
                print(f"Producto '{nombre}' añadido al carrito.")
                return
            else:
                print(f"No hay suficiente cantidad de '{nombre}'. Disponible: {producto[2]}.")
                return
    print(f"El producto '{nombre}' no se encuentra en la tienda.")

def ver_carrito(carrito):
    if not carrito:
        print("El carrito está vacío.")
    else:
        print("\nProductos en el carrito:")
        total = 0
        for item in carrito:
            subtotal = item[1] * item[2]
            print(f"Nombre: {item[0]}, Cantidad: {item[1]}, Precio: {item[2]:.2f} €, Subtotal: {subtotal:.2f} €")
            total += subtotal
        print(f"Total en el carrito: {total:.2f} €\n")

def finalizar_compra(carrito):
    if not carrito:
        print("No hay productos en el carrito para finalizar la compra.")
        return
    total = sum(item[1] * item[2] for item in carrito)
    print(f"Gracias por tu compra. Total a pagar: {total:.2f} €")
    carrito.clear()  # Vaciar el carrito

def cancelar_compra(carrito):
    if not carrito:
        print("No hay productos en el carrito para cancelar.")
        return
    carrito.clear()  # Vaciar el carrito
    print("Compra cancelada. El carrito está vacío.")

def menu_cliente(productos, carrito):
    while True:
        print("1. Mostrar productos disponibles")
        print("2. Comprar productos")
        print("3. Ver carrito")
        print("4. Finalizar compra")
        print("5. Cancelar compra")
        print("6. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            mostrar_productos(productos)
        elif opcion == '2':
            comprar_producto(productos, carrito)
        elif opcion == '3':
            ver_carrito(carrito)
        elif opcion == '4':
            finalizar_compra(carrito)
        elif opcion == '5':
            cancelar_compra(carrito)
        elif opcion == '6':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def menu_vendedor(productos, historial):
    while True:
        print("1. Mostrar productos disponibles")
        print("2. Agregar producto")
        print("3. Eliminar producto")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            mostrar_productos(productos)
        elif opcion == '2':
            agregar_producto(productos, historial)
        elif opcion == '3':
            eliminar_producto(productos, historial)
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def main():
    productos = []  # Lista para almacenar productos
    historial = []  # Lista para almacenar historial de productos eliminados
    carrito = []    # Lista para el carrito de compras

    # Autenticación del vendedor
    while True:
        perfil = input("Selecciona tu perfil (cliente/vendedor): ").strip().lower()
        if perfil == 'vendedor':
            password = input("Introduce la contraseña del vendedor: ")
            if password == "vendedor123":  # Contraseña de acceso para el vendedor
                print("Acceso concedido. Bienvenido vendedor.")
                menu_vendedor(productos, historial)
                break
            else:
                print("Contraseña incorrecta. Intenta de nuevo.")
        elif perfil == 'cliente':
            print("Bienvenido cliente.")
            menu_cliente(productos, carrito)
            break
        else:
            print("Perfil no válido. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
