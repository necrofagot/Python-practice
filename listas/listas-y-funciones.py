import random

lista_example = []
n = int(input('Ingrese cantidad de numeros a generar'))

#Generar lista random
for _ in range(n):
    numero = random.randint(1,200)
    lista_example.append(numero)


#Generar el numero aureo en una lista de N numeros con una funcion:
def fibonacci(lista):
    if len(lista) != 0:
        return 'Su lista debe estar vacia!'
    lista = [0,1]
    for _ in range(n - 2): #Resto 2 por que la lista ya posee 0 y 1.
        lista.append(lista[-1] + lista[-2])
    return lista

#imprimir los multiplos de un numero x:
def multi(lista,x):
    multi = []
    for num in lista:
        if num % x == 0:
            multi.append(num)
    return multi

#Hacer una funcion que diga cual es el tercer elemento, me diga la cantidad de elementos y si la lista esta vacia:
def listado_checking(lista, index):
    if len(lista) == 0:
        return 'Su lista esta vacia'
    return f'El {index} elemento de su lista es:{lista[index]} y su lista contiene {len(lista)} elementos'

#Funcion que reconozca palindromos:
def palindromo(str):
    strpal = str.lower().replace(' ','')
    return strpal == strpal[::-1]

#Funcion para sacar factorial
def factorial(lista):
    lista_f = []
    for num in lista:
        aux = num
        for i in range (1,num):
            aux = aux * (num - i)
        lista_f.append(aux)
    return lista_f