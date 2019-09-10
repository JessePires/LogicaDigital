def porta_and(entradas):

    for entrada in entradas:
        if(entrada == 0):
            return 0
    
    return 1

def porta_or(entradas):

    for entrada in entradas:
        if(entrada == 1):
            return 1
    
    return 0

def porta_not(entrada):

    1 if entrada == 0 else 0
    return entrada

def porta_xor(entradas):

    if entradas[0] == entradas[1]:

        return 0

    return 1

def porta_nor(entradas):

    if entradas[0] == entradas[1]:

        return 1

    return 0

# exercício 1
def e_um(a, b, c, d):

    primeira_parte = porta_not(porta_or([a, porta_not(b), c]))
    segunda_parte = porta_or([a, porta_not(d), b])
    terceira_parte = porta_not(porta_and([primeira_parte, segunda_parte]))
    s = porta_and([terceira_parte, porta_not(a), b, porta_not(c)])

    print("O resultado da expressão do exercício 1 é: ", s)

# exercício 2
def e_dois(a, b, c, d):

    primeira_parte = porta_nor([a, b])
    segunda_parte = porta_not(porta_or([porta_not(a), primeira_parte, porta_not(d)]))
    terceira_parte = porta_not(porta_and([porta_not(b), d, porta_not(d)]))
    s = porta_or([segunda_parte, porta_not(d), terceira_parte])

    print("O resultado do exercício 2 é: ", s)

