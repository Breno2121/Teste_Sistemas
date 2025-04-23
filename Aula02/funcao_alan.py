def validar_cadastro(nome,telefone, email, idade):
   return " " in nome and "48" in telefone and "@" in email and idade >= 18


def validar_salario(salario, comissao, inss):
   return salario + (salario * comissao) - (salario * inss)
