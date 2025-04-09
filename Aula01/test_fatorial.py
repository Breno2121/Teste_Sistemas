import pytest 
from Aula01.fatorial import fatorial

@pytest.mark.parametrize("fator, expected", [(3, 6),(4, 24),(5, 120),(6, 720)])

def test_factor(fator, expected):
    assert fatorial(fator) == expected