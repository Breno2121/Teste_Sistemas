from questao05 import *


def test_validar_nivel_funcionario():
    assert idade_votar(12) == "NAO PODE VOTAR"
    assert idade_votar(16) == "PODE VOTAR"
    assert idade_votar(18) == "DEVE VOTAR MAS NAO PODE SER PRESIDENTE"
    assert idade_votar(70) == "DEVE VOTAR E PODE SER PRESIDENTE"
    assert idade_votar(75) == "PODE VOTAR E PODE SER PRESIDENTE"


