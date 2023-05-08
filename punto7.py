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
    