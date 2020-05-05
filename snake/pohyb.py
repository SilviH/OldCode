def strany(souradnice, ss):

    a = souradnice[len(souradnice)-1][0]
    b = souradnice[len(souradnice)-1][1]

    if ss == 's':
        souradnice.append((a - 1, b))
    elif ss == 'j':
        souradnice.append((a + 1, b))
    elif ss == 'v':
        souradnice.append((a, b + 1))
    elif ss == 'z':
        souradnice.append((a, b - 1))
