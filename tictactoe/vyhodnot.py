def vyhodnot(hra):
    '''dostane řetězec s herním polem 1-D piškvorek,
     a vrátí jednoznakový řetězec podle stavu hry'''
    if 'xxx' in hra and 'ooo' not in hra:
        return 'x'
    elif 'ooo' in hra and 'xxx' not in hra:
        return 'o'
    elif 'xxx' in hra and 'ooo' in hra:
        return '!'
    else:
        return '–'
