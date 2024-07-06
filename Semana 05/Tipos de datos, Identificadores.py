# Este programa calcula el área de un círculo basado en el radio proporcionado por el usuario.

import math

def calcular_area(radio):
    """Calcula el área de un círculo dado su radio."""
    area = math.pi * (radio ** 2)
    return area

def main():
    # Solicita al usuario que ingrese el radio del círculo
    radio_circulo = float(input("Introduce el radio del círculo: "))
    # Calcula el área
    area = calcular_area(radio_circulo)
    # Muestra el resultado
    print(f"El área del círculo con radio {radio_circulo} es {area:.2f}")

if __name__ == "__main__":
    main()






