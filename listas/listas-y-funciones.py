import random

lista_example = []
n = int(input('Ingrese cantidad de numeros a generar'))

#Generar lista random
def lista_random(lista):
    for _ in range(n):
        numero = random.randint(1,200)
        lista.append(numero)

#Generar el numero aureo en una lista de N numeros con una funcion:
def fibonacci(lista):
    if len(lista) != 0:
        return 'Su lista debe estar vacia!'
    lista = [0,1]
    for _ in range(n - 2): #Resto 2 por que la lista ya posee 0 y 1.
        lista.append(lista[-1] + lista[-2])
    return lista

#Hacer una funcion que diga cual es el tercer elemento, me diga la cantidad de elementos y si la lista esta vacia:
def listado_checking(lista):
    if len(lista) == 0:
        return 'Su lista esta vacia'
    return f'El tercer elemento de su lista es:{lista[2]} y su lista contiene {len(lista)} elementos'

#Funcion que reconozca palindromos:
def palindromo(str):
    for i in range(len(str) // 2):
        if str[i] != str[-(i + 1)]:
            return False
    return True     
#No funciona! tengo que borrar los espacios en blanco!