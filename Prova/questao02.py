
def nivel(salario, cargo, tempoEmpresa, matricula):
    if salario <= 4000 and tempoEmpresa < 5 :
        funcao = "JUNIOR"
        return {"Desenvolvedor ": funcao}
    elif salario > 4000 and salario < 10000 or tempoEmpresa > 5 and tempoEmpresa <= 10 :
        funcao = "PLENO"
        return {"Desenvolvedor ": funcao}
    elif salario > 10000  or tempoEmpresa > 10 :
        funcao = "SENIOR"
        return {"Desenvolvedor ": funcao}
     
