import pytest

import tah_pocitace

def test_tah_chyba():
    with pytest.raises(ValueError):
        tah_pocitace.tah_pocitace('oxoxoxoxoxoxoxoxoxox')
