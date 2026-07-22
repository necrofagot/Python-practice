with open('D:/archivos_Python/txt/example.txt','w') as example:
    cod_Demon = input('Ingrese un numeor de identificacion o Enter para finalizar')
    while cod_Demon != '':
        cod_De2 = cod_Demon
        soul_Eated = timestaed = 0
        while cod_Demon == cod_De2:
            namDem = input('Ingrese su nombre')
            soul_Eated += int(input('Almas consumidas'))
            timestaed += 1
            cod_Demon = input('Codigo de demonio o enter')
        example.write(f'{cod_De2},{namDem},{soul_Eated},{timestaed}\n')

with open('D:/archivos_Python/txt/example.txt','r') as exampleR:
    documento = exampleR.readline()
    while documento != '':    
        linea = documento.strip().split(',')
        cod_Demon = linea[0]
        soul_Eated = timestaed = 0
        while documento != '' and cod_Demon == linea[0]:
            soul_Eated += int(linea[2])
            timestaed += int(linea[3])
            namDem = linea[1]
            if documento != '': linea = documento.strip().split(',')
        prom = soul_Eated / timestaed
        print(f'El demonio {namDem} comio {soul_Eated} almas en {timestaed} veces, con un promedio de {prom} almas por vez')
