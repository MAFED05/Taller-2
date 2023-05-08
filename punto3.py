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
