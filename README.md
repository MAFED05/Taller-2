# Taller #2
Bug.Ing

Taller realizado por: Maria Fernanda Duarte Parra, Cristian Felipe Gutiérrez Espitia y John Steven Padilla Goyes

## Punto 1

Desarrollar un programa que ingrese un número entero n y separe todos los digitos que componen el número.

#### Solución

``` python
n = int(input("Ingrese un número entero: ")) #Se solicita que ingrese un dato
listaDeDigitos = [] #Se crea un lista sin datos
while n > 0: #Mientras el número ingresado sea mayor de 0 entonces
    Digito = n % 10 #Se realiza un modulo
    listaDeDigitos.append(Digito) #El append en este caso funciona para añadir el digito a la lista
    n //= 10 # El dato se divide en 10 y se continua con el proceso
listaDeDigitos.reverse() #Se coloca la lista al reves para que de esta manera aparezcan en el orden correcto
print ("Los dígitos del número ingresado son:") #Se imprime un enunciado
for Digito in listaDeDigitos: 
    print(Digito) #Se imprimen los dígitos
```

### Código funcionando

## Punto 2

Desarrollar un programa que ingrese un número flotante n y separe su parte entera de la parte decimal, y luego entrege los digitos tanto de la parte entera como de la decimal.

#### Solución

``` python
# Solicitamos al usuario que ingrese un número flotante y lo convertimos en float
numero = float(input("Ingrese un número flotante: "))

# Obtenemos la parte entera del número flotante utilizando la función int() y almacenamos en la variable parte_entera
parte_entera = int(numero)

# Obtenemos la parte decimal del número flotante restando la parte entera al número original y tomando el valor absoluto con la función abs()
parte_decimal = abs(numero - parte_entera)

# Imprimimos los dígitos de la parte entera del número
print("Dígitos de la parte entera:")
# Convertimos la parte entera en una cadena y utilizamos un bucle for para imprimir cada dígito en una línea separada
for digito in str(parte_entera):
    print(digito)

# Imprimimos los dígitos de la parte decimal del número
print("Dígitos de la parte decimal:")
# Convertimos la parte decimal en una cadena, y utilizamos un bucle for para imprimir cada dígito de la parte decimal en una línea separada
# Usamos [2:] para omitir los dos primeros caracteres '0.' en la parte decimal.
for digito in str(parte_decimal)[2:]:
    print(digito)
```

### Código funcionando

## Punto 3

Desarrollar un programa que permita ingresar dos números enteros y determinar si se tratan de números espejos


#### Solución

``` python
# El usuario ingresa el primer número
numero1 = int(input("Por favor ingrese un numero:   "))
# El usuario ingresa el segundo número
numero2 = int(input("Por favor ingrese un numero:   "))

# Define una función llamada 'espejo' que toma dos argumentos: n y m
def espejo(k,x):  
  # Asigna el valor de 'numero1' a la variable 'k'
  k = numero1
  # Inicializa una cadena vacía llamada 'espejo'
  espejo = ""
  # Ejecuta el bucle mientras 'k' sea mayor que 0
  while(k>0):
    # Obtiene el último dígito de 'k' y lo asigna a la variable 'dig'
    dig = k%10
    # Elimina el último dígito de 'k' y lo asigna a la variable 'sig'
    sig = k//10
    # Convierte el dígito obtenido en cadena y lo asigna a la variable 'x'
    x = str(dig)
    # Agrega el dígito como cadena al final de la cadena 'espejo'
    espejo+=x
    # Actualiza el valor de 'k' con el valor de 'sig'
    k = sig
  # Compara si la cadena 'espejo' es igual a la representación en cadena de 'numero2'
  if(espejo == str(numero2)):
    # Si son iguales, imprime que los números son espejo entre sí
    print(f"El número {numero1} y el número {numero2} son números espejo entre sí")
  else:
    # Si no son iguales, imprime que los números no son espejo entre sí
    print(f"El número {numero1} y el número {numero2} no son números espejo entre sí")

# Llama a la función 'espejo' con los valores de 'numero1' y 'numero2'
espejo(numero1,numero2)
```

### Código funcionando

## Punto 4

Diseñar una función que permita calcular una aproximación de la función coseno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Taylor. nota: use math para traer la función coseno y mostrar la diferencia entre el valor real y la aproximación. Con cuántos valores de la serie, se tienen errores del 10%, 1%, 0.1% y 0.001%.

#### Solución

``` python
import math #Se importa la primera libreria
def punto4(x:float, n:int) -> float:
    real = math.cos(x) #Se importa el coseno desde math
    aprox = 0
    errorA = "No suficiente para obtener un error de menos del 10%"
    errorB = "No suficiente para obtener un error de menos del 1%"
    errorC = "No suficiente para obtener un error de menos del 0.1%"
    errorD = "No suficiente para obtener un error de menos del 0.001%"
    #Se colocan los rangos y demás para determinar los valores de error y demás 
    for i in range(n+1):
        aprox += ((-1)**i) * (x**(2*i)) / (math.factorial(2*i))
        if round(aprox, 5) == round(real, 5):
            errorA = i
        elif round(aprox, 3) == round(real, 3):
            errorB = i
        elif round(aprox, 2) == round(real, 2):
            errorC = i
        elif round(aprox, 1) == round(real, 1):
            errorD = i
            break

     
    diff = real - aprox
    main = "real: " + str(real) + " aprox: " + str(aprox) + " diff: " + str(diff) + " error A: " + str(errorA) + " error B: " + str(errorB) + " error C: " + str(errorC) + " error C: " + str(errorD) 
    return main
if __name__ == "__main__":
    x = float(input("Ingrese un número real "))
    n = int(input("Ingrese un número entero: "))
    main = punto4(x, n)
    print(main)
```

### Código funcionando

## Punto 5

Desarrollar un programa que permita determinar el Minimo Comun Multiplo de dos numeros enteros. Abordar el problema desde la perpectiva iterativa como recursiva.

#### Solución 1

``` python
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

```

### Código funcionando 1


#### Solución 2

``` python
#PUNTO_5_PERSPECTIVA_RECURSIVA

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

```

### Código funcionando 2

## Punto 6

Desarrollar un programa que determine si en una lista no existen elementos repetidos.


#### Solución

``` python
# Inicializa una lista vacía llamada 'elementos_x' para almacenar los elementos ingresados por el usuario
elementos_x = []
# Inicializa una lista vacía llamada 'repetidos' para almacenar los elementos repetidos encontrados
repetidos = []

# Inicia un bucle infinito que se ejecutará hasta que el usuario decida detenerlo
while True:
    # Solicita al usuario que ingrese un elemento para la lista, uno por uno
    elemento = input("Ingrese los elementos de la lista uno por uno. Cuando haya terminado, simplemente presione Enter.")
    # Verifica si el usuario ingresó una cadena vacía (presionó Enter sin ingresar nada)
    if elemento == "":
        # Si el usuario ingresó una cadena vacía, sale del bucle infinito
        break
    # Si el usuario ingresó un elemento, se agrega a la lista 'elementos_x'
    elementos_x.append(elemento)

# Itera sobre cada elemento en la lista 'elementos_x'
for i in elementos_x:
    # Verifica si el elemento 'i' aparece más de una vez en la lista 'elementos_x'
    # y si 'i' no está en la lista 'repetidos' (para evitar duplicados en la lista 'repetidos')
    if elementos_x.count(i) > 1 and i not in repetidos:
        # Si se cumplen ambas condiciones, agrega el elemento 'i' a la lista 'repetidos'
        repetidos.append(i)

# Verifica si la lista 'repetidos' está vacía
if len(repetidos) == 0:
    # Si está vacía, imprime que no hay elementos repetidos en la lista
    print("En esta lista no existen elementos repetidos")
else:
    # Si no está vacía, imprime los elementos repetidos encontrados
    print("Los elementos repetidos son:", repetidos)

```

### Código funcionando

## Punto 7

Desarrollar un programa que determine si en una lista se encuentra una cadena de caracteres con dos o más vocales. Si la cadena existe debe imprimirla y si no existe debe imprimir 'No existe'.

#### Solución

``` python
'''
Desarrollar un programa que determine si en una lista se encuentra una cadena de caracteres con dos o más vocales. 
Si la cadena existe debe imprimirla y si no existe debe imprimir 'No existe'.
'''

def encontrarVocales(lista:list) -> list: #Se define la función
    vocalesCadenas = [] # se crea una lista para guradar las cadenas que puedan tener más de 2 vocales.
    for elemento in lista: #Para cada elemento de la lista
        if type(elemento) == str: #Se revisa que el dato se trate de un str
            contador = [dato for dato in elemento if dato in "AEIOUaeiou"] # se guardan las vocales del elemento x en una lista.
            if len(contador) > 1: # si hay más de una, se añade el elemento a la lista de vocales.
                vocalesCadenas.append(elemento)
    if len(encontrarVocales) == 0: # si no se guardaron elementos en la lista de vocales, se retorna que como resultado que no existe.
        return "No existe"
    else:
        return vocalesCadenas # En caso contrario se devuelven las vocales encontradas en la lista
    
if __name__ == "__main__": #Se define la función principal
    lista = []
    n = int(input("Ingrese el número de elementos que va a tener la lista: ")) #Se le solicita al usuario que ingrese cuantos datos va a tener la lista
    for x in range(n): #Se delimita un rango
        elemento = input("Ingrese un elemento: ") #Se le solicita al usuario que ingrese un elemento
        lista.append(elemento) #Se añade el elemento a la lista
    main = encontrarVocales(lista) 
    print(main) #Se imprime lo necesario
```

### Código funcionando


## Punto 8

Desarrollar un programa que dadas dos listas determine que elementos tiene la primer lista que no tenga la segunda lista.

#### Solución

``` python
'''
Desarrollar un programa que dadas dos listas determine que elementos tiene la primer lista que no tenga la segunda lista.
'''

def listaFinal(lista1:list, lista2:list) -> list: #Se define la primera función donde estará la tercera lista

    lista3 = [] # se crea una lista para guardar los elementos que no sean comunes entre las dos listas.
    for elemento in lista1: #Para cada elemento de la lista 1
        if elemento not in lista2: #si el elemento de la lista1 no está en la lista2, se agrega a lista3.
            lista3.append(elemento)#Se agrega el elemento a la lista 3

    return lista3 #Devuelve la lista 3

if __name__ == "__main__": #Se define la función principal
    lista1 = [] #Lista 1 vacia
    lista2 = [] #Lista 2 vacia
    n = int(input("Ingrese el número de elementos que va a tener cada lista: ")) #Se pregunta al usuario cuantos elementos tendrá cada lista
    for x in range(n): #Se delimita el rango
        elemento = input("Ingrese un elemento para la lista 1: ") #Se ingresan los datos de la primera lista
        lista1.append(elemento) #Se añaden los elementos a la lista 1
    for x in range(n): #Se delimita el rango para la segunda lista
        elemento = input("Ingrese un elemento para la lista 2: ") #Se ingresan los datos de la segunda lista
        lista2.append(elemento) #Se añaden esos elementos a la segunda lista
    main = listaFinal(lista1, lista2) #Se le indica al programa que deberá retornar la lista final
    print(main) #Se imprimen los elementos
```

### Código funcionando

## Punto 9

Resolver el punto 7 del taller 1 usando operaciones con vectores.

#### Solución

``` python
# Pedir 5 números reales al usuario
numeros = []
for i in range(5):
    num = float(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)

# Calcular el promedio aritmético
promedio_aritmetico = sum(numeros) / len(numeros)

# Calcular la mediana
numeros_ordenados = sorted(numeros)
mediana = 0
if len(numeros_ordenados) % 2 == 0:
    # Si el número de elementos es par, se promedian los dos del centro
    indice_medio = len(numeros_ordenados) // 2
    mediana = (numeros_ordenados[indice_medio-1] + numeros_ordenados[indice_medio]) / 2
else:
    # Si el número de elementos es impar, se toma el del centro
    indice_medio = len(numeros_ordenados) // 2
    mediana = numeros_ordenados[indice_medio]

# Calcular el promedio multiplicativo
producto = 1
for num in numeros:
    producto *= num
promedio_multiplicativo = pow(producto, 1/len(numeros))

# Ordenar los números de forma ascendente
numeros_ascendente = sorted(numeros)

# Ordenar los números de forma descendente
numeros_descendente = sorted(numeros, reverse=True)

# Calcular la potencia del mayor número elevado al menor número
mayor = max(numeros)
menor = min(numeros)
potencia = mayor ** menor

# Calcular la raíz cúbica del menor número
raiz_cubica = pow(menor, 1/3)

# Mostrar los resultados
print(f"El promedio aritmético es: {promedio_aritmetico}")
print(f"La mediana es: {mediana}")
print(f"El promedio multiplicativo es: {promedio_multiplicativo}")
print(f"Los números en orden ascendente son: {numeros_ascendente}")
print(f"Los números en orden descendente son: {numeros_descendente}")
print(f"El mayor número elevado al menor número es: {potencia}")
print(f"La raíz cúbica del menor número es: {raiz_cubica}")
```

### Código funcionando
## Punto 10

Desarrollar un algoritmo que determine si una matriz es mágica. Se dice que una matriz cuadrada es mágica si la suma de cada una de sus filas, de cada una de sus columnas y de cada diagonal es igual.

#### Solución

``` python
def es_matriz_magica(matriz):
    # La suma de la primera fila se usa como referencia para todas las demás sumas.
    suma_referencia = sum(matriz[0])

    # Comprueba las filas.
    for fila in matriz:
        if sum(fila) != suma_referencia:
            return False

    # Comprueba las columnas.
    for i in range(len(matriz)):
        if sum(fila[i] for fila in matriz) != suma_referencia:
            return False

    # Comprueba la diagonal principal.
    if sum(matriz[i][i] for i in range(len(matriz))) != suma_referencia:
        return False

    # Comprueba la diagonal secundaria.
    if sum(matriz[i][len(matriz)-i-1] for i in range(len(matriz))) != suma_referencia:
        return False

    return True

def ingresar_matriz():
    n = int(input("Ingrese el tamaño de la matriz cuadrada (n x n): "))
    matriz = []
    for _ in range(n):
        fila = list(map(int, input("Ingrese la matriz por filas:").split()))
        matriz.append(fila)
    return matriz

def main():
    matriz = ingresar_matriz()
    
    if es_matriz_magica(matriz):
        print("La matriz es mágica.")
    else:
        print("La matriz no es mágica.")

if __name__ == "__main__":
    main()
```

### Código funcionando
