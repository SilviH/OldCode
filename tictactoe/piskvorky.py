from random import randrange
import tah_hrace
import tah_pocitace
import vyhodnot

def piskvorky1d():
# vytvoření pole
    pole = 20 * '-'
    while vyhodnot.vyhodnot(pole) != 'o' and vyhodnot.vyhodnot(pole) != 'x' and vyhodnot.vyhodnot(pole) != '!':
            pole = (tah_hrace.tah_hrace(pole))
            pole = (tah_pocitace.tah_pocitace(pole))
            print(pole)
            print(vyhodnot.vyhodnot(pole))
