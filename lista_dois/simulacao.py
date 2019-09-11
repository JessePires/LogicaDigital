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

    return porta_not(porta_or(entradas))

def porta_nand(entradas):

    return porta_not(porta_and(entradas))

# exercício 1
def e_um(a, b, c, d):

    primeira_parte = porta_not(porta_or([a, porta_not(b), c]))
    segunda_parte = porta_or([a, porta_not(d), b])
    terceira_parte = porta_not(porta_and([primeira_parte, segunda_parte]))
    s = porta_and([terceira_parte, porta_not(a), b, porta_not(c)])

    print("Resultado da expressão do exercício 1 é: ", s)

# exercício 2
def e_dois(a, b, c, d):

    primeira_parte = porta_nor([a, b])
    segunda_parte = porta_not(porta_or([porta_not(a), primeira_parte, porta_not(d)]))
    terceira_parte = porta_not(porta_and([porta_not(b), d, porta_not(d)]))
    s = porta_or([segunda_parte, porta_not(d), terceira_parte])

    print("Resultado do exercício 2 com as entradas [", a, ", ", b , ", ", c , ", ", d, "] : ", s)    

#exercício 5
def e_cinco(a, b, c, d):

    primeira_parte = porta_nor([a, porta_not(d)])
    segunda_parte = porta_and([primeira_parte, b])
    terceira_parte = porta_and([porta_not(a), b, porta_not(c)])
    quarta_parte = porta_and([b, porta_not(c)])
    quinta_parte = porta_and([porta_not(b), c])
    sexta_parte = porta_nor([segunda_parte, terceira_parte, quarta_parte, quinta_parte])
    setima_parte = porta_xor([b, c])
    oitava_parte = porta_and([sexta_parte, setima_parte])
    nona_parte = porta_and([a, b, d])
    decima_parte = porta_nor([oitava_parte, nona_parte, porta_not(b)])
    decima_primeira_parte = porta_or([porta_not(a), porta_not(b)])
    s = porta_and([decima_parte, decima_primeira_parte])
    
    print("Resultado do exercício 11 com as entradas [", a, ", ", b, ", ", c, ", ", d, "] : ", s)    

#exercício 11
def e_onze(a, b, c, d):

    primeira_parte = porta_nand([a, b, c, d])
    segunda_parte = porta_and([porta_not(a), b, porta_not(c), d])
    terceira_parte = porta_and([porta_not(a), b, c, porta_not(d)])
    quarta_parte = porta_and([a, b, porta_not(c), d])
    quinta_parte = porta_and([a, b, c, d])
    s = porta_or([primeira_parte, segunda_parte, terceira_parte, quarta_parte, quinta_parte])

    print("Resultado do exercício 11 com as entradas [", a, ", ", b, ", ", c, ", ", d, "] : ", s)    

#exercício 12
def e_doze(a, b, c, d):

    primeira_parte = porta_and([porta_not(a), b, porta_not(c), d])
    segunda_parte = porta_and([porta_not(a), b, c, porta_not(d)])
    terceira_parte = porta_and([a, porta_not(b), porta_not(c), porta_not(d)])
    quarta_parte = porta_and([a, porta_not(b), b, c])
    s = porta_or([primeira_parte, segunda_parte, terceira_parte, quarta_parte])

    print("Resultado do exercício 12 com as entradas [", a, ", ", b, ", ", c, ", ", d, "] : ", s)    

# exercício 26
def e_vinte_seis(a, b, c):

    primeira_parte = porta_and([a, b, c,])
    segunda_parte = porta_and([a, b, porta_not(c)])
    terceira_parte = porta_and([a, porta_not(b), c])
    quarta_parte = porta_and([porta_not(a), b, c])
    s = porta_or([primeira_parte, segunda_parte, terceira_parte, quarta_parte])

    print("Resultado do exercício 26 com as entradas [", a, ", ", b , ", ", c , "] : ", s)

#exercicio 27
def e_vinte_sete(a, b):

    negacao_a = porta_nor([a, a])
    negacao_b = porta_nor([b, b])
    primeira_parte = porta_nor([negacao_a, b])
    segunda_parte = porta_nor([a, negacao_b])
    terceira_parte = porta_nor([primeira_parte, segunda_parte])
    s = porta_nor([terceira_parte, terceira_parte])

    print("Resultado do exercício 27 com as entradas [", a, ", ", b, "] : ", s)    

#exercício 28
def e_vinte_oito(a, b):

    negacao_a = porta_nand([a, a])
    negacao_b = porta_nand([b, b])
    primeira_parte = porta_nand([a, b])
    segunda_parte = porta_nand([negacao_a, negacao_b])
    terceira_parte = porta_nand([primeira_parte, segunda_parte])
    s = porta_nand([terceira_parte, terceira_parte])

    print("Resultado do exercício 28 com as entradas [", a, ", ", b, "] : ", s)    

