def primos(num):
    for x in range(2,num):
        if num % x == 0:
            return 0
    return num

def multi(num):
    if num % 3 == 0:
            return num
    return 0

with open("D:/Python-practice/txt/ctonicRegister.txt",'r') as ctonic_r, open("D:/Python-practice/txt/ctonicRegisterTotal2.txt", 'w') as ctonic_w:
    document = ctonic_r.readline()
    while document != "":
        lines = document.strip().split(',')
        name = lines[0]
        souls = 0
        while document != "" and name == lines[0]:
            souls += float(lines[1])
            document = ctonic_r.readline()
            if document != "": lines = document.strip().split(',')
        ctonic_w.write(f'{name}, {souls:.2f}\n')
