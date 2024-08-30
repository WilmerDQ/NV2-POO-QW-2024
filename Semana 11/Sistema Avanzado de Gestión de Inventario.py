import json


# Clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def obtener_info(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio


# Clase Inventario
class Inventario:
    def __init__(self):
        self.productos = {}  # Usamos un diccionario para almacenar los productos, donde el ID es la clave

    def agregar_producto(self, producto):
        if producto.id_producto in self.productos:
            print("El producto con ese ID ya existe.")
        else:
            self.productos[producto.id_producto] = producto
            print("Producto añadido con éxito.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("Producto eliminado con éxito.")
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        if id_producto in self.productos:
            if nueva_cantidad is not None:
                self.productos[id_producto].actualizar_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                self.productos[id_producto].actualizar_precio(nuevo_precio)
            print("Producto actualizado con éxito.")
        else:
            print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        for producto in self.productos.values():
            if producto.nombre.lower() == nombre.lower():
                print(producto.obtener_info())
                return producto
        print("Producto no encontrado.")
        return None

    def mostrar_todos_los_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos.values():
                print(producto.obtener_info())

    # Métodos para almacenar en archivos
    def guardar_en_archivo(self, nombre_archivo):
        try:
            with open(nombre_archivo, 'w') as archivo:
                productos_serializados = {id_: vars(producto) for id_, producto in self.productos.items()}
                json.dump(productos_serializados, archivo)
                print("Inventario guardado en archivo con éxito.")
        except Exception as e:
            print(f"Error guardando el archivo: {e}")

    def cargar_desde_archivo(self, nombre_archivo):
        try:
            with open(nombre_archivo, 'r') as archivo:
                productos_serializados = json.load(archivo)
                for id_producto, datos in productos_serializados.items():
                    producto = Producto(**datos)
                    self.productos[id_producto] = producto
                print("Inventario cargado desde archivo con éxito.")
        except FileNotFoundError:
            print("Archivo no encontrado.")
        except Exception as e:
            print(f"Error cargando el archivo: {e}")


# Interfaz de usuario en consola
def menu():
    inventario = Inventario()

    while True:
        print("\n--- Menú de Gestión de Inventario ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario en archivo")
        print("7. Cargar inventario desde archivo")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
        elif opcion == '2':
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == '3':
            id_producto = input("ID del producto a actualizar: ")
            nueva_cantidad = input("Nueva cantidad (deje vacío para no cambiar): ")
            nuevo_precio = input("Nuevo precio (deje vacío para no cambiar): ")
            inventario.actualizar_producto(
                id_producto,
                int(nueva_cantidad) if nueva_cantidad else None,
                float(nuevo_precio) if nuevo_precio else None
            )
        elif opcion == '4':
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)
        elif opcion == '5':
            inventario.mostrar_todos_los_productos()
        elif opcion == '6':
            nombre_archivo = input("Nombre del archivo para guardar: ")
            inventario.guardar_en_archivo(nombre_archivo)
        elif opcion == '7':
            nombre_archivo = input("Nombre del archivo para cargar: ")
            inventario.cargar_desde_archivo(nombre_archivo)
        elif opcion == '8':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")


# Ejecución del programa
if __name__ == "__main__":
    menu()
