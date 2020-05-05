def tah(pole, pozice, symbol):
    "Vrátí herní pole s daným symbolem umístěným na danou pozici"

    return pole[:pozice] + symbol + pole[pozice + 1:]
