# Definición de la clase base Persona con encapsulación del atributo edad
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.__edad = edad  # Atributo privado

    def mostrar_info(self):
        print(f'Nombre: {self.nombre}, Edad: {self.__edad}')

    def obtener_edad(self):
        return self.__edad


# Definición de la clase derivada Estudiante, demostrando herencia
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    # Sobreescritura del método mostrar_info para incluir la carrera del estudiante
    def mostrar_info(self):
        super().mostrar_info()
        print(f'Carrera: {self.carrera}')


# Ejemplo de polimorfismo con la función imprimir_info
def imprimir_info(persona):
    persona.mostrar_info()


# Creación de instancias de las clases y demostración de su funcionalidad
persona = Persona('Wilmer', 29)
estudiante = Estudiante('Danilo', 20, 'Ingeniería')

# Llamada a la función polimórfica con diferentes tipos de objetos
imprimir_info(persona)
imprimir_info(estudiante)
