class ClimaSemanal:
    def __init__(self):
        """
        Inicializa una nueva instancia de la clase ClimaSemanal con una lista vacía para almacenar temperaturas.
        """
        self.temperaturas = []

    def ingresar_temperaturas(self):
        """
        Método para ingresar las temperaturas diarias de la semana.
        """
        for i in range(7):  # Suponemos una semana de 7 días
            while True:
                try:
                    temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
                    self.temperaturas.append(temp)
                    break
                except ValueError:
                    print("Entrada no válida. Por favor, ingrese un número.")

    def calcular_promedio(self):
        """
        Método para calcular el promedio de las temperaturas ingresadas.
        """
        if not self.temperaturas:
            return 0
        total = sum(self.temperaturas)
        promedio = total / len(self.temperaturas)
        return promedio

    def mostrar_temperaturas(self):
        """
        Método para mostrar las temperaturas ingresadas.
        """
        return self.temperaturas

    def mostrar_promedio(self):
        """
        Método para mostrar el promedio de las temperaturas.
        """
        promedio = self.calcular_promedio()
        return promedio


def main():
    print("Programa para calcular el promedio semanal del clima")

    # Crear una instancia de ClimaSemanal
    clima_semanal = ClimaSemanal()

    # Ingresar las temperaturas diarias
    clima_semanal.ingresar_temperaturas()

    # Mostrar las temperaturas ingresadas
    temperaturas = clima_semanal.mostrar_temperaturas()
    print(f"Las temperaturas ingresadas son: {temperaturas}")

    # Calcular y mostrar el promedio semanal
    promedio_semanal = clima_semanal.mostrar_promedio()
    print(f"El promedio semanal de las temperaturas es: {promedio_semanal:.2f}")


if __name__ == "__main__":
    main()
