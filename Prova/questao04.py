def realizarOperacao(valor01, sinal, valor02):
    if sinal == "+":
        return valor01 + valor02
    elif sinal == "-":
        return valor01 - valor02
    elif sinal == "*":
        return valor01 * valor02
    elif sinal == "/":
       if valor02 == 0:
           return "Divisão por zero não é possível."
       else:
           return valor01 / valor02
    else:
        return "Sinal inválido."
    