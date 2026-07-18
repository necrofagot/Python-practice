#Hacer una funcion que diga cual es el tercer elemento, me diga la cantidad de elementos y si la lista esta vacia:
import random
n = int(input('Ingrese cantidad de numeros a generar'))
listorta = [20]
for i in range(n):
    numero = random.randint(1,200)
    listorta.append(numero)
print(listorta)
def listado_checking(lista):
    if len(lista) == 0:
        return 'Su lista esta vacia'
    return f'El tercer elemento de su lista es:{lista[2]} y su lista contiene {len(lista)} elementos'

print(listado_checking(listorta))
