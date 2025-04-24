import pytest
from questao04 import *

@pytest.mark.parametrize("valor01, sinal, valor02, resultado_esperado", [
    (10, "*", 2, 20),                  
    (5, "+", 5, 10),                     
    (10, "/", 0, "Divisão por zero não é possível."),  
    (10, "/", 2, 5),                     
    (5, "-", 3, 2),                       
    (7, "@", 2, "Sinal inválido.")        
])
def test_realizarOperacao(valor01, sinal, valor02, resultado_esperado):
    assert realizarOperacao(valor01, sinal, valor02) == resultado_esperado


