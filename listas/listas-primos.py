#Ingrese un numero entero llamado N que sea la cantidad de elementos que tendra una lista de numeros enteros entre 1 y 100.000. luego mediante una funcion que genere una lista con los numeros primos de la lista generada y luego recorrer la lista y obtener la posicion relativa de los maximos, los valores deben ser grabados en otra lista, retornar de la funcion ambas listas obtenidas y mostrarla fuera de la funcion.
import random

n = int(input('ingrese un numero entero N: '))
lista_numeros = []

for i in range(n):
    numero_random = random.randint(1, 100000)
    lista_numeros.append(numero_random)

def primos(lista):
    lista_primos = lista[:] 
    lista_posicion = []
    pos = 0
    for numero_l in lista:
        if numero_l == max(lista):
            lista_posicion.append(pos)
        pos += 1
        for i in range(2, numero_l):
            if numero_l % i == 0:
                lista_primos.remove(numero_l)
                break
    return lista_primos, lista_posicion

print(primos(lista_numeros))
