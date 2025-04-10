

def calculadora(valor1, valor2, sinal):

    if(sinal == "+"):
        resultado = (valor1 + valor2)
        return resultado
    elif(sinal == "-"):
        resultado = (valor1 - valor2)
        return resultado
    elif(sinal == "*"):
        resultado = (valor1 * valor2)
        return resultado
    elif(sinal == "/"):
        resultado = (valor1 / valor2)
        return resultado
    
print(calculadora(45,5, '/'))