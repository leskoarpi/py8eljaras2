'''
2. Feladat
Írj eljárást, amely paraméterül kapott számról eldönti, és a képernyőre kiírja, hogy negatív, pozitív vagy nulla-e!
'''
def donto(szam):
    if int(szam) < 0:
        print(f'a megadott szam "{szam}" negatív')
    if int(szam) > 0:
        print(f'a megadott szam "{szam}" pozitív')
    else:
        print('A megadott szam 0')