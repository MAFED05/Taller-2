n = int(input("Ingrese un número entero: "))
listaDeDigitos = []
while n > 0:
    Digito = n % 10
    listaDeDigitos.append(Digito)
    n //= 10
listaDeDigitos.reverse()
print ("Los dígitos del número ingresado son:")
for Digito in listaDeDigitos:
    print(Digito)