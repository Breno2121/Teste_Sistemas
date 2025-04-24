
def idade_votar(idade):
    
    if idade < 16:
        return "NAO PODE VOTAR"
    elif idade == 16 or idade == 17 :
        return "PODE VOTAR"
    elif idade >= 18 and idade <= 34 :
        return "DEVE VOTAR MAS NAO PODE SER PRESIDENTE"
    elif idade > 34 and idade < 71 :
        return "DEVE VOTAR E PODE SER PRESIDENTE"
    elif idade > 70 :
        return "PODE VOTAR E PODE SER PRESIDENTE"
    

