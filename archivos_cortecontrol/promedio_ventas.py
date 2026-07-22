with open("D:/archivos_Python/txt/docum.txt",'r') as ventas, open("D:/archivos_Python/txt/docum2.txt",'w') as promedio:
    docVentas = ventas.readline() 
    while docVentas != '':
        lineas = docVentas.strip().split(',') #Lee una linea y la transforma en una lista separando por comas
        legajo = lineas[0]
        ventas = cantVentas = 0
        while docVentas != '' and legajo == lineas[0]:
            ventas += int(lineas[1]) #El formato de docum.txt es: legajo,ventas
            cantVentas += 1
            if docVentas != '': lineas = docVentas.strip().split(',')
        prom = ventas / cantVentas
        promedio.write(f'{legajo},{ventas},{cantVentas},{prom}\n')
