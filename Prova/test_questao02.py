from questao02 import *

    
def test_validar_nivel_funcionario():
    assert nivel(1000, "pedreiro", 2, 16184) == {'Desenvolvedor ': 'JUNIOR'}
    assert nivel(3500, "pedreiro", 6, 16184) == {'Desenvolvedor ': 'PLENO'}
    assert nivel(10000, "pedreiro", 12, 16184) == {'Desenvolvedor ': 'SENIOR'}


