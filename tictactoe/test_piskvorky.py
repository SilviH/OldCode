import tah_pocitace

def test_tah_na_prazdne_pole():
    pole = tah_pocitace.tah_pocitace('--------------------')
    assert len(pole) == 20
    assert pole.count('o') == 1
    assert pole.count('-') == 19
