from random import randrange

def tah_pocitace(pole):
    "Vrátí herní pole se zaznamenaným tahem počítače"
    for i in range(20):
        pozice = randrange(20)

        while pole[pozice] == 'x' or pole[pozice] == 'o':
            pozice = randrange(20)
#strategie
        if pole[pozice - 1] == 'x':
            return pole[:pozice] + 'o' + pole[pozice + 1:]
        elif pozice == 19:
            pass
        elif pole[pozice + 1] == 'x':
            return pole[:pozice] + 'o' + pole[pozice + 1:]

    return pole[:pozice] + 'o' + pole[pozice + 1:]
