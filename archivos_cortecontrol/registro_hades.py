with open('D:/Python_practice/txt/ctonicRegister.txt','w') as ctonico_w:
    daemon = input('Ingrese nombre de la entidad o Enter para finalizar ').lower()
    while daemon != '':
        dactual = daemon
        total = 0
        while dactual == daemon:
            almas = int(input('Cuantas almas consumio?'))
            total += almas
            daemon = input('Ingrese nombre de la entidad o Enter para finalizar ').lower()
            ctonico_w.write(f'{dactual},{total}\n')

with open('D:/Python-practice/txt/ctonicRegister.txt','r') as ctonico_r, open('D:/Python-practice/txt/ctonicRegisterTotal.txt','w') as totalctonico:
    doctonico = ctonico_r.readline()
    while doctonico != '':
        linea = doctonico.strip().split(',')
        dactual = linea[0]
        total = 0
        while doctonico != '' and dactual == linea[0]:
            total += int(linea[1])
            if doctonico != '': linea = doctonico.strip().split(',')
        totalctonico.write(f'{dactual},{total}\n')
