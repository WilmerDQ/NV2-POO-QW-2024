class Persona:
    def __init__(self, nombre, edad):
        # Constructor: inicializa los atributos de la clase
        self.nombre = nombre
        self.edad = edad
        print(f"Persona {self.nombre} ha sido creada.")

    def __del__(self):
        # Destructor: se ejecuta cuando se elimina una instancia de la clase
        print(f"Persona {self.nombre} ha sido eliminada.")

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

# Crear una instancia de la clase Persona
persona1 = Persona("Juan", 30)
persona1.mostrar_info()

# Eliminar la instancia de la clase Persona
del persona1
