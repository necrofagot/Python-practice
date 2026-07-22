with open("D:/Python-practice/txt/ventas_x_cliente.txt","w+") as ventasPcleinte:
    
    while False:
        nroClientes = int(input('numero cliente: '))
        razoncliente = input('nombre clienta: ')
        cantVentas = int(input('ventas cliente: '))
        if nroClientes == 505: break
        ventasPcleinte.write(f'{nroClientes},{cantVentas},{razoncliente}\n')

with open("D:/Python-practice/txt/ventas_x_cliente.txt","r") as ventasPcleinte, open("D:/Python-practice/txt/acumulado_x_cliente.txt", "w") as acumuladoPcliente:
    docVentas = ventasPcleinte.readline()

    while docVentas != '':
        lineas = docVentas.strip().split(",")
        nroClientes = lineas[0]
        totalAcumulado = cantVentas = 0
        while docVentas != '' and nroClientes == lineas[0]:
            totalAcumulado += int(lineas[2])
            razoncliente = lineas[1]
            cantVentas += 1
            if docVentas != '': lineas = docVentas.strip().split(",")
        acumuladoPcliente.write(f'{nroClientes},{totalAcumulado},{razoncliente}\n')