"""
    Implementação do multiplicador de valores binários

    Aluno: Jessé P. B. Rocha

    R.A: 2149389
"""

registrador = [0]   


def validacao(entrada):
    for x in entrada:
        if x > 1 or x < 0:
            return False


def porta_or(*entrada):
    if validacao(entrada) == False:
        return False

    aux = 0
    for x in entrada:
        aux = x or aux
    return aux


def porta_and(*entrada):
    if validacao(entrada) == False:
        return False

    aux = 1
    for x in entrada:
        aux = x and aux
    return aux


def porta_not(a):
    if a > 1 or a < 0:
        return False

    if a == 0:
        return 1
    else:
        return 0


def porta_nand(*entrada):
    if validacao(entrada) == False:
        return False

    i = porta_and(*entrada)
    return porta_not(i)


def porta_nor(*entrada):
    if validacao(entrada) == False:
        return False

    i = porta_or(*entrada)
    return porta_not(i)


def porta_xor(*entrada):
    if validacao(entrada) == False:
        return False

    s = 0
    for x in entrada:
        if s != x:
            s = 1
        else:
            s = 0
    return s


def porta_xnor(*entrada):
    if validacao(entrada) == False:
        return False

    s = 1
    for x in entrada:
        if s == x:
            s = 1
        else:
            s = 0
    return s


def somador(a, b, c_in):

    s = porta_xor(a, b, c_in)
    cout = porta_or(porta_and(a, b), porta_and(b, c_in), porta_and(a, c_in))

    return s, cout


def soma(m, a):

    c_out = 0

    for i in range(len(m)-1, -1, -1):
        m[i], c_out = somador(m[i], a[i], c_out)

    return m, c_out


def configura_registrador():

    m = []
    q = []

    multiplicando = input("Digite, em binário, o valor do multiplicando: ")
    multiplicador = input("Digite, em binário, o valor do multiplicador: ")
    
    
    for i in multiplicando:
        m.append(i)

    for i in multiplicador:
        q.append(i)

    for i in range(len(m)):
        registrador.append(0)
    
    for i in q:
        registrador.append(i)

    return m, len(q)


def shift():

    for i in range(len(registrador) -1, -1, -1):
        registrador[i] = registrador[i-1]


def main():

    m, tam_q = configura_registrador()

    for i in registrador:
        print(i)

    s, c_out = soma(m, registrador[1:5:1])

    for i in range(tam_q):
        if registrador[-1] == 1:
            registrador[1:5:1], registrador[0] = soma(registrador[1:5:1], m)
        shift()

    print("\nResultado: ", end = " ")
    for i in registrador:
        print(i, end = "")
    print()

main()
            