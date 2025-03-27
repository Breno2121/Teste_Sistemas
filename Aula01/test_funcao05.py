from funcao import *


def test_verifica_maiusculo():
    assert verifica_maiusculo("ABC") is True
    assert verifica_maiusculo("abc") is False
    assert verifica_maiusculo("") is False


##EXEMPLO PROFESSOR
# def test_maiuscula():
#     if any(x.isupper()for x in nome):
#         return False

