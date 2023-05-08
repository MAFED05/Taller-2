# PUNTO_5
# Define la función para encontrar el máximo común divisor de dos números enteros
def mcd(a, b):
    # Mientras b no sea cero:
    while b != 0:     # Usamos While para implementar el algoritmo de Uclides y así encontrar el MCD de dos números enteros
        # Encuentra el residuo de la división entera de a entre b
        r = a % b
        # Actualiza el valor de a con el valor actual de b
        a = b
        # Actualiza el valor de b con el valor actual de r
        b = r
    # Retorna el último valor no cero de b, que es el máximo común divisor
    return a

# Define la función para encontrar el mínimo común múltiplo de dos números enteros
def mcm(a, b):
    # Utiliza la relación entre el máximo común divisor y el mínimo común múltiplo para encontrar el resultado
    return (a * b) // mcd(a, b)

# Pide al usuario que ingrese dos números enteros y los convierte a enteros
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Imprime el mínimo común múltiplo de num1 y num2 utilizando la función mcm
print("El mínimo común múltiplo de", num1, "y", num2, "es:", mcm(num1, num2))



