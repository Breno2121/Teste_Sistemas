
def coleta_dados(nome, idade, telefone, email):
    if " " in nome and "48" in telefone and "@" in email:
        return {
            "nome": nome,
            "idade": idade,
            "telefone": telefone,
            "email": email
        }
    

def coleta_salario(salario, comissao, inss):
    salario_bruto = salario + (salario * (comissao / 100))
    desconto_inss = salario * (inss / 100)
    salario_liquido = salario_bruto - desconto_inss

    return {
        "salario_bruto": salario_bruto,
        "desconto_inss": desconto_inss,
        "salario_liquido": salario_liquido
     }
