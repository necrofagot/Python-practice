listorta = [100,50,400,500]

def lista_change(lista):
    act=input('A o R')
    nwmero= int(input('numero'))
    if act.lower() == 'a':
        act=input('I o C o A')
        if act.lower() == 'i':
            indekz=int(input('index'))
            return lista.insert(indekz,nwmero)
        elif act.lower() == 'c':
            indekz=int(input('index'))
            lista[indekz] = nwmero
            return lista
        else:
            return lista.append(nwmero)
    elif act.lower() == 'r':
        act=input('Q')
        if act.lower() == 'q':
            indekz=int(input('index'))
            return lista.pop(indekz)
        else:
            return lista.remove(nwmero)

lista_change(listorta)
print(listorta) 
