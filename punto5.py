#PUNTO_5_PERSPECTIVA_RECURSUVA

# Definimos la función mcd que toma dos argumentos a y b y devuelve su máximo común divisor utilizando el algoritmo de Euclides de manera recursiva
def mcd(a, b):
    if b == 0:  # si b es cero, devuelve a como resultado
        return a
    else:  # si b no es cero, se llama a sí misma con b como primer argumento y el residuo de a/b como segundo argumento
        return mcd(b, a % b)

# Definimos la función mcm que toma dos argumentos a y b y devuelve su mínimo común múltiplo utilizando la relación entre el mcm y el mcd
def mcm(a, b):
    return (a * b) // mcd(a, b)  # utilizamos la relación mcm = (a * b) / mcd(a, b) para encontrar el resultado

# Pedimos al usuario que ingrese dos números enteros y los convertimos en enteros utilizando la función int
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Imprimimos el resultado utilizando la función mcm y print
print("El mínimo común múltiplo de", num1, "y", num2, "es:", mcm(num1, num2))
