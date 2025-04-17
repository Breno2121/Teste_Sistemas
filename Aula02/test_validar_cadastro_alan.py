from funcao_alan import *


def test_validar_cadastro_funciona():
    assert validar_cadastro("Breno silva", "48996146493", "josebrenosilva0@gmail.com", 25) == True


def test_validar_cadastro_funciona():
    resultado = validar_salario( 3000, 10, 5 )
    assert resultado == 18000