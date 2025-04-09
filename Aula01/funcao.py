def email_valido(email):
    return "@" in email and ".com" in email

def dividir(a, b):
    if b == 0:
        return None
    return a/b

def verifica_maiusculo(maiusculo):
    return maiusculo[1].isupper() if maiusculo else False

for i in range(3):
    print(f"Iteração {i}")


# def test_maiuscula():
# assert maiuscula("Breno") == True

