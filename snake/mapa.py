from random import randrange
def vytvor_tabulku(souradnice,ovoce,ocasek,kolo, bonus):
    seznam_radku = []
    for a in range(10):
        radek = []
        for b in range(10):
            radek.append('.')
        seznam_radku.append(radek)

    for i in range(len(souradnice)):
        c = souradnice[i][0]
        d = souradnice[i][1]
        seznam_radku[c][d] = 'X'


# ovoce
    while seznam_radku[ovoce[0][0]][ovoce[0][1]] == 'X':
        u = randrange(10)
        v = randrange(10)
        ovoce.clear()
        ovoce.append((u,v))
        souradnice[:0] = [ocasek]
        souradnice
    seznam_radku[ovoce[0][0]][ovoce[0][1]] = '?'

    # nové ovoce po 20kolech
    if kolo % 30 == 0 and kolo != 0:
        bonus1 = randrange(10)
        bonus2 = randrange(10)
        bonus.append((bonus1,bonus2))
    if bonus:
        if seznam_radku[bonus[0][0]][bonus[0][1]] == 'X':
                bonus.clear()
                souradnice[:0] = [ocasek]

    if bonus:
        seznam_radku[bonus[0][0]][bonus[0][1]] = '?'

    a = souradnice[len(souradnice)-1][0]
    b = souradnice[len(souradnice)-1][1]
    seznam_radku[a][b] = 'O'
# Vypsání celé tabulky
    for radek in seznam_radku:
        for tecka in radek:
            print(tecka, end=' ')
        print()
