import os

class Producto:
    def __init__(self, id_producto, nombre, cantidad):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad

    def __str__(self):
        return f'{self.id_producto},{self.nombre},{self.cantidad}'


class Inventario:
    def __init__(self, archivo_inventario='inventario.txt'):
        self.archivo_inventario = archivo_inventario
        self.productos = self.cargar_inventario()

    def cargar_inventario(self):
        productos = []
        if os.path.exists(self.archivo_inventario):
            try:
                with open(self.archivo_inventario, 'r') as archivo:
                    for linea in archivo:
                        datos = linea.strip().split(',')
                        if len(datos) == 3:
                            id_producto, nombre, cantidad = datos
                            productos.append(Producto(id_producto, nombre, int(cantidad)))
                print(f"Inventario cargado desde {self.archivo_inventario}.")
            except FileNotFoundError:
                print("Archivo de inventario no encontrado.")
            except PermissionError:
                print("No tienes permisos para leer el archivo de inventario.")
            except Exception as e:
                print(f"Error inesperado al leer el archivo: {e}")
        else:
            print("El archivo de inventario no existe. Se creará uno nuevo al guardar productos.")
        return productos

    def guardar_inventario(self):
        try:
            with open(self.archivo_inventario, 'w') as archivo:
                for producto in self.productos:
                    archivo.write(str(producto) + '\n')
            print("Inventario guardado correctamente.")
        except PermissionError:
            print("No tienes permisos para escribir en el archivo de inventario.")
        except Exception as e:
            print(f"Error inesperado al guardar el archivo: {e}")

    def agregar_producto(self, id_producto, nombre, cantidad):
        producto = Producto(id_producto, nombre, cantidad)
        self.productos.append(producto)
        try:
            self.guardar_inventario()
            print(f"Producto {nombre} añadido exitosamente.")
        except Exception as e:
            print(f"Error al añadir producto: {e}")

    def eliminar_producto(self, id_producto):
        productos_filtrados = [producto for producto in self.productos if producto.id_producto != id_producto]
        if len(productos_filtrados) == len(self.productos):
            print("Producto no encontrado.")
            return
        self.productos = productos_filtrados
        try:
            self.guardar_inventario()
            print(f"Producto con ID {id_producto} eliminado correctamente.")
        except Exception as e:
            print(f"Error al eliminar producto: {e}")

    def actualizar_producto(self, id_producto, cantidad):
        for producto in self.productos:
            if producto.id_producto == id_producto:
                producto.cantidad = cantidad
                try:
                    self.guardar_inventario()
                    print(f"Producto {producto.nombre} actualizado correctamente.")
                except Exception as e:
                    print(f"Error al actualizar producto: {e}")
                break
        else:
            print("Producto no encontrado.")

    def mostrar_productos(self):
        if self.productos:
            print("Inventario actual:")
            for producto in self.productos:
                print(f"ID: {producto.id_producto}, Nombre: {producto.nombre}, Cantidad: {producto.cantidad}")
        else:
            print("El inventario está vacío.")


# Función principal para interactuar con el sistema de inventario
def main():
    inventario = Inventario()

    while True:
        print("\n--- Sistema de Gestión de Inventarios ---")
        print("1. Ver inventario")
        print("2. Añadir producto")
        print("3. Eliminar producto")
        print("4. Actualizar producto")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            inventario.mostrar_productos()
        elif opcion == '2':
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            inventario.agregar_producto(id_producto, nombre, cantidad)
        elif opcion == '3':
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == '4':
            id_producto = input("ID del producto a actualizar: ")
            cantidad = int(input("Nueva cantidad: "))
            inventario.actualizar_producto(id_producto, cantidad)
        elif opcion == '5':
            print("Saliendo del sistema de gestión de inventarios.")
            break
        else:
            print("Opción no válida, por favor selecciona una opción válida.")

if __name__ == "__main__":
    main()
