import mapa
import pohyb
souradnice = [(0,0),(1,0),(2,0)]
ovoce = [(2,3)]
ocasek = 0
kolo = 0
bonus = []
mapa.vytvor_tabulku(souradnice,ovoce,ocasek,kolo,bonus)

while True:
    kolo = kolo + 1
    ocasek = souradnice[0]
    del souradnice[0]
    ss = input('Světová strana:')
    pohyb.strany(souradnice,ss)
    if souradnice[len(souradnice)-1][0] < 0 or souradnice[len(souradnice)-1][0] > 9 or \
    souradnice[len(souradnice)-1][1] < 0 or souradnice[len(souradnice)-1][1] > 9:
        print('Mimo pole!\nGame Over.')
        break
    if souradnice[len(souradnice) - 1] in souradnice[:len(souradnice) - 1]:
        print('Kousl ses!\nGame Over.')
        break
    mapa.vytvor_tabulku(souradnice,ovoce,ocasek,kolo,bonus)
