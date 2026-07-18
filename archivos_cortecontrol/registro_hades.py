with open('D:/archivos_Python/txt/ctonicRegister.txt','w') as ctonico_w:
    daemon = input('Ingrese nombre de la entidad o Enter para finalizar ').lower()
    while daemon != '':
        dactual = daemon
        cm = total = 0
        while dactual == daemon:
            almas = int(input('Cuantas almas consumio?'))
            total += almas
            daemon = input('Ingrese nombre de la entidad o Enter para finalizar ').lower()
            ctonico_w.write(f'{dactual},{total}\n')
        
with open('D:/archivos_Python/txt/ctonicRegister.txt','r') as ctonico_r, open('D:/archivos_Python/txt/ctonicRegisterTotal.txt','w') as totalctonico:
      x = 0
      linea = ctonico_r.readlines()
      dato = linea[x].strip().split(',')
      while x <= len(linea):
          total = 0
          dactual = dato[0]
          while dactual == dato[0]:
              print('entre')
              dato = linea[x].strip().split(',')
              x +=1
              total += int(dato[1])
              print(total)
              print(dato,x)
          totalctonico.write(f'{dactual},{total}\n')
      
