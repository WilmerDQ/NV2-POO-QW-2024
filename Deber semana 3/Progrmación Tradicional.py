
def ingresar_temperaturas():
    """
    Función para ingresar las temperaturas diarias de la semana.
    Retorna una lista de temperaturas.
    """
    temperaturas = []
    for i in range(7):  # Suponemos una semana de 7 días
        while True:
            try:
                temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número.")
    return temperaturas


def calcular_promedio(temperaturas):
    """
    Función para calcular el promedio de una lista de temperaturas.
    """
    if len(temperaturas) == 0:
        return 0
    total = sum(temperaturas)
    promedio = total / len(temperaturas)
    return promedio


def mostrar_resultados(temperaturas, promedio):
    """
    Función para mostrar las temperaturas y el promedio calculado.
    """
    print(f"Las temperaturas ingresadas son: {temperaturas}")
    print(f"El promedio semanal de las temperaturas es: {promedio:.2f}")


def main():
    print("Programa para calcular el promedio semanal del clima")

    # Ingresar las temperaturas diarias
    temperaturas = ingresar_temperaturas()

    # Calcular el promedio semanal
    promedio_semanal = calcular_promedio(temperaturas)

    # Mostrar los resultados
    mostrar_resultados(temperaturas, promedio_semanal)


if __name__ == "__main__":
    main()
