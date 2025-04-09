def fatorial(fator):
  
    aux= fator
    total= fator
    while aux > 1:
        total*= aux-1
        aux -= 1
    return total