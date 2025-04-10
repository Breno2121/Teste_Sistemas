def peso_altura(peso,altura):
    imc = peso/(altura*altura)

    if imc < 17:
        RESULTADO = "muito abaixo do peso ideal"
    elif imc >= 17 and imc <= 18.49:
        RESULTADO = "abaixo do peso"
    elif imc  >= 18.5 and  imc <= 24.99:
        RESULTADO = "peso normal"
    elif imc >= 25 and imc <= 29.99:
        RESULTADO = "acimo do peso"
    elif imc >= 30 and imc <= 34.99:
        RESULTADO = "Obesidade grou 1"
    elif imc >= 35 and imc <= 39.99:
        RESULTADO = "Obesidade grou 2"
    else:
        RESULTADO = "Obesidade grau 3(Mórbida)"

    return RESULTADO
print(peso_altura(21,100))