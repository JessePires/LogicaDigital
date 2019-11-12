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


def porta_xnor(entradas):

    return porta_not(porta_xor(entradas))


def somador_subtrator(a, b, op, c_in, decoder):

    primeira_parte_s =  porta_and([decoder, porta_and([porta_and([c_in, porta_xnor([a, b])])])])
    segunda_parte_s = porta_and([porta_not(c_in), porta_xor([a, b])])
    s = porta_or([primeira_parte_s, segunda_parte_s])

    primeira_parte_cout = porta_and([a, porta_or([porta_and([porta_not(op), porta_and([decoder, porta_or([c_in, b])])]), porta_and([b, c_in])])])
    segunda_parte_cout = porta_and([porta_not(a), porta_and([op, porta_or([porta_and([porta_not(c_in), b]), porta_and([c_in, decoder])])])])
    terceira_parte_cout = porta_and([b, c_in, decoder])
    cout = porta_or([primeira_parte_cout, segunda_parte_cout, terceira_parte_cout])

    return s, cout


def decoder(f0, f1, f2):

    s_and = porta_and([porta_not(f0), porta_not(f1), porta_not(f2)])
    s_or = porta_and([porta_not(f0), porta_not(f1), f2])
    s_not = porta_and([porta_not(f0), f1, porta_not(f2)])
    s_nand = porta_and([porta_not(f0), f1, f2])
    s_nor = porta_and([f0, porta_not(f1), porta_not(f2)])
    s_xor = porta_and([f0, porta_not(f1), f1])
    s_soma_subtrator = porta_or([porta_and([f0, f1]), porta_and([f0, f1])])
    s_op = f2

    return s_and, s_or, s_not, s_nand, s_nor, s_xor, s_soma_subtrator, s_op 


def logical_unit(a, b, in_and, in_or, in_not, in_nand, in_nor, in_xor):

    s_and = porta_and([porta_and([a, b], in_and])
    s_or = porta_and([porta_or([a, b]), in_or])
    s_not = porta_and([porta_not(b), in_not])
    s_nand = porta_and([porta_nand([a, b]), in_nand])
    s_nor = porta_and([porta_nor([a, b]), in_nor])
    s_xor = porta_and([porta_xor([a, b]), in_xor])

    return s_and, s_or, s_not, s_nand, s_nor, s_xor


def ula_1_bit(f0, f1, f2, a, b, c_in, c_out):

    s_and, s_or, s_not, s_nand, s_nor, s_xor, s_soma_subtrator, s_op = decoder(f0, f1, f2)
    s_a, s_b, s_and, s_or, s_not, s_nand, s_nor, s_xor = logical_unit(a, b, s_and, s_or, s_not, s_nand, s_nor, s_xor)
    soma, c_out = somador_subtrator(s_a, s_b, s_op, c_in, s_soma_subtrator)
    
    s = porta_or([s_and, s_or, s_not, s_nand, s_nor, s_xor, soma])

    return s, c_out


