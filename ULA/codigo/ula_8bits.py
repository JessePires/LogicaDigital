import math
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

def somador_subtrator(a, b, op, c_in, decoder):

    primeira_parte_s =  porta_and(decoder, porta_and(porta_and(c_in, porta_xnor(a, b))))
    segunda_parte_s = porta_and(porta_not(c_in), porta_xor(a, b))
    s = porta_or(primeira_parte_s, segunda_parte_s)

    primeira_parte_cout = porta_and(a, porta_or(porta_and(porta_not(op), porta_and(decoder, porta_or(c_in, b))), porta_and(b, c_in)))
    segunda_parte_cout = porta_and(porta_not(a), porta_and(op, porta_or(porta_and(porta_not(c_in), b), porta_and(c_in, decoder))))
    terceira_parte_cout = porta_and(b, c_in, decoder)
    cout = porta_or(primeira_parte_cout, segunda_parte_cout, terceira_parte_cout)

    return s, cout


def decoder(f0, f1, f2):

    s_and = porta_and(porta_not(f0), porta_not(f1), porta_not(f2))
    s_or = porta_and(porta_not(f0), porta_not(f1), f2)
    s_not = porta_and(porta_not(f0), f1, porta_not(f2))
    s_nand = porta_and(porta_not(f0), f1, f2)
    s_nor = porta_and(f0, porta_not(f1), porta_not(f2))
    s_xor = porta_and(f0, porta_not(f1), f1)
    s_soma_subtrator = porta_or(porta_and(f0, f1), porta_and(f0, f1))
    s_op = f2

    return s_and, s_or, s_not, s_nand, s_nor, s_xor, s_soma_subtrator, s_op 


def logical_unit(a, b, in_and, in_or, in_not, in_nand, in_nor, in_xor):

    s_and = porta_and(porta_and(a, b), in_and)
    s_or = porta_and(porta_or(a, b), in_or)
    s_not = porta_and(porta_not(b), in_not)
    s_nand = porta_and(porta_nand(a, b), in_nand)
    s_nor = porta_and(porta_nor(a, b), in_nor)
    s_xor = porta_and(porta_xor(a, b), in_xor)

    return a, b, s_and, s_or, s_not, s_nand, s_nor, s_xor


def ula_1_bit(f0, f1, f2, a, b, c_in):

    s_and, s_or, s_not, s_nand, s_nor, s_xor, s_soma_subtrator, s_op = decoder(f0, f1, f2)
    s_a, s_b, s_and, s_or, s_not, s_nand, s_nor, s_xor = logical_unit(a, b, s_and, s_or, s_not, s_nand, s_nor, s_xor)
    soma, c_out = somador_subtrator(s_a, s_b, s_op, c_in, s_soma_subtrator)
    
    s = porta_or(s_and, s_or, s_not, s_nand, s_nor, s_xor, soma)

    return s, c_out


def conversor_dec_bin(num):

    bin_invertido = []
    bin_correto = []

    while num > 0:

        bin_invertido.append(num % 2)
        num = num // 2

    while len(bin_invertido) < 8:

        bin_invertido.append(0)

    for i in range(len(bin_invertido) -1, -1, -1):

        bin_correto.append(bin_invertido[i])
    
    return bin_correto


def conversor_bin_dec(vet_bin):

    dec = 0
    c = 7
    for num in vet_bin:
        if num == 1:
            dec += math.pow(2, c)
        c -= 1

    return int(dec)


def separador_de_bits(dec):

    centena = dec // 100
    dezena = (dec % 100) // 10
    unidade = (dec % 100) % 10

    return centena, dezena, unidade



def ula_8bits(f0, f1, f2, a ,b ,s):
    
    s[7], c_out1 =  ula_1_bit(f0, f1, f2, a[7], b[7], 0)
    s[6], c_out2 =  ula_1_bit(f0, f1, f2, a[6], b[6], c_out1)
    s[5], c_out3 =  ula_1_bit(f0, f1, f2, a[5], b[5], c_out2)
    s[4], c_out4 =  ula_1_bit(f0, f1, f2, a[4], b[4], c_out3)
    s[3], c_out5 =  ula_1_bit(f0, f1, f2, a[3], b[3], c_out4)
    s[2], c_out6 =  ula_1_bit(f0, f1, f2, a[2], b[2], c_out5)
    s[1], c_out7 =  ula_1_bit(f0, f1, f2, a[1], b[1], c_out6)
    s[0], c_out8 =  ula_1_bit(f0, f1, f2, a[0], b[0], c_out7)
    return c_out8


def main():

    f0 = 1
    f1 = 1
    f2 = 1

    a = 128
    b = 1

    s_bin = [0,0,0,0,0,0,0,0]

    c_out8 = ula_8bits(f0, f1, f2, conversor_dec_bin(a) ,conversor_dec_bin(b), s_bin)
    
    if c_out8 == 1:
        print("Estouro")
    else:
        for num in s_bin:
            print(num, end=" ")
        print("\n")
    
    s_dec = conversor_bin_dec(s_bin)
    print(s_dec)
main()
