with open("D:/archivos_Python/docum.txt",'r') as ventas, open("D:/archivos_Python/docum2.txt",'w') as promedio:
    docVentas = ventas.readlines() #Transforma el archivo en una lista
    i = 0
    while i < len(docVentas):
        lineas = docVentas[i].strip().split(',') #Lee una linea y la transforma en una lista separando por comas
        legajo = lineas[0]
        ventas = cantVentas = 0
        while legajo == lineas[0]:
            ventas += int(lineas[1]) #El formato de docum.txt es: legajo,ventas
            cantVentas += 1
            i += 1
            if i == len(docVentas): break #Evita el error de indice fuera de rango
            lineas = docVentas[i].strip().split(',')
        prom = ventas / cantVentas
        promedio.write(f'{legajo},{ventas},{cantVentas},{prom}\n')
