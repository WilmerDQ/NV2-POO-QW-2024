from inventario import Inventario
from producto import Producto


def menu():
    print("\nSistema de Gestión de Inventarios")
    print("1. Añadir nuevo producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto")
    print("5. Mostrar todos los productos")
    print("6. Salir")


def main():
    inventario = Inventario()

    while True:
        menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            id = input("Introduce el ID del producto: ")
            nombre = input("Introduce el nombre del producto: ")
            cantidad = int(input("Introduce la cantidad del producto: "))
            precio = float(input("Introduce el precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            try:
                inventario.añadir_producto(producto)
                print("Producto añadido exitosamente.")
            except ValueError as e:
                print(e)

        elif opcion == '2':
            id = input("Introduce el ID del producto a eliminar: ")
            inventario.eliminar_producto(id)
            print("Producto eliminado exitosamente.")

        elif opcion == '3':
            id = input("Introduce el ID del producto a actualizar: ")
            cantidad = input("Introduce la nueva cantidad (deja en blanco si no se actualiza): ")
            precio = input("Introduce el nuevo precio (deja en blanco si no se actualiza): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            try:
                inventario.actualizar_producto(id, cantidad, precio)
                print("Producto actualizado exitosamente.")
            except ValueError as e:
                print(e)

        elif opcion == '4':
            nombre = input("Introduce el nombre del producto a buscar: ")
            resultados = inventario.buscar_producto(nombre)
            if resultados:
                for producto in resultados:
                    print(producto)
            else:
                print("No se encontraron productos.")

        elif opcion == '5':
            inventario.mostrar_productos()

        elif opcion == '6':
            print("Saliendo del sistema.")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    main()
