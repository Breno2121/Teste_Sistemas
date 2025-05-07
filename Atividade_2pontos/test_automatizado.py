import unittest

from Aluno import Aluno
from financeiro import Financeiro
from Nota import Nota

class TestAluno(unittest.TestCase):
    def setUp(self):
        self.aluno = Aluno("jose")
        self.aluno.adicionar_nota(6)
        self.aluno.adicionar_nota(10)

    def test_calcular_media(self):
        self.assertEqual(self.aluno.calcular_media(), 8.0)

class TestFinanceiro(unittest.TestCase):
    def setUp(self):
        self.financeiro = Financeiro()
        self.financeiro.adicionar_valor_devido(450)
        self.financeiro.adicionar_valor_pago(270)

    def test_calcular_valor_em_aberto(self):
        self.assertEqual(self.financeiro.calcular_valor_em_aberto(), 180)

if __name__ == "__main__":
    unittest.main()
