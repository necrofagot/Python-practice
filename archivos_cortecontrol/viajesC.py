with open('D:/archivos_Python/practica/viajesCombi.txt', 'w') as viajes:
    namEmp = input('Ingrese Nombre de la Empresa, al finalizar precione enter\n')
    while namEmp != '':
        codEmp = input('Codigo Empresa\n')
        canTravel = input('Cuantos Viajes\n')
        recaudo = input('Cuanto Recaudo\n')
        viajes.write(f'{codEmp},{namEmp},{canTravel},{recaudo}\n')
        namEmp = input('Ingrese otro Nombre de Empresa o precione enter\n')    

with open('D:/archivos_Python/practica/viajesCombi.txt', 'r') as viajesR:
    documento = viajesR.readlines()
    i = ultrecaudo = 0
    while i < len(documento):
        linea = documento[i].strip().split(',') #lee la linea i
        codEmp = linea[0]
        canTravel = recaudo = 0
        while codEmp == linea[0]:
            namEmp = linea[1]
            canTravel += int(linea[2])
            recaudo += int(linea[3])
            i += 1
            if i == len(documento): break
            linea = documento[i].strip().split(',') #lee la linea i
        print(f'{namEmp} realizó {canTravel} y recaudó {recaudo}\n')
        if recaudo > ultrecaudo:
            ultrecaudo = recaudo
            empRecaudo = namEmp 
    print(f'{empRecaudo} recaudo {ultrecaudo} siendo la mayor en recaudar.\n')