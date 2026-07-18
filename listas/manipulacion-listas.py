lista_nueva = [100,50,400,500]

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
        elif act.lower() == 'a':
            return lista.append(nwmero)
    elif act.lower() == 'r':
        act=input('Q o R')
        if act.lower() == 'q':
            indekz=int(input('index'))
            return lista.pop(indekz)
        elif act.lower() == 'r':
            return lista.remove(nwmero)

#El if me hace ruido y no estoy seguro si el return esta bien o no.

lista_change(lista_nueva)
print(lista_nueva)
