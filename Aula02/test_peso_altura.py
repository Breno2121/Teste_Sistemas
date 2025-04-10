import pytest
from verificação_altura_peso import peso_altura

# def test_peso_normal():
#     resultado = peso_altura(70, 1.75)
#     assert resultado == "peso normal"


@pytest.mark.parametrize("peso,altura,esperado",[
    (45, 1.70, "muito abaixo do peso ideal"),
    (53, 1.70, "abaixo do peso"),
    (65, 1.70, "peso normal"),
    (77, 1.70, "acimo do peso"),
    (90, 1.70, "Obesidade grou 1"),
    (102, 1.70, "Obesidade grou 2"),
    (280, 1.75, "Obesidade grau 3(Mórbida)")
    ])

def test_peso_altura(peso,altura,esperado):
    assert peso_altura(peso,altura) == esperado