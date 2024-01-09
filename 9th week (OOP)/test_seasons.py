import pytest
from seasons import yesssir

def test():
    assert yesssir("1999-01-01")=="Thirteen million, one hundred sixty thousand, one hundred sixty minutes"
    assert yesssir("1998-01-01")=="Thirteen million, six hundred eighty-five thousand, seven hundred sixty minutes"
