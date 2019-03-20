import pytest
from principal import mult
from principal import div

def test_multi ():
    assert mult (2,5)==10

def test_divi ():
    assert div (10,2)==5
