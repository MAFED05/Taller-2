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