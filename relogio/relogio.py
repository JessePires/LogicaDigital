from time import sleep
import math
from datetime import datetime
now = datetime.now()


def p_nand_2(a, b):
    return int(not(a and b))

def p_nand_3(a, b, c):
    return int(not(a and b and c))

def p_not(a):
    return int(not(a))

def ff_jk(ck=1, j=1, k=1, qa=0):
    qa1, qa2 = qa, p_not(qa)
    qf1, qf2 = qa1, qa2
    while True:
        s1 = p_nand_3(j, ck, qa2)
        s2 = p_nand_3(k, ck, qa1)
        qf1 = p_nand_2(s1, qf2)
        qf2 = p_nand_2(s2, qf1)
        if qf1 != qf2:
            return qf1

def segmentos_7(v):
    s = lambda desenho, existe: desenho if int(existe) else ' '
    inter = ('', '.', '', '.', '', ' ', '', '')
    l1, l2, l3 = '', '', ''
    v = [nb[v[i:i+4]] for i in range(0, len(v), 4)]
    for i, c in enumerate((0, 0, 1, 0, 1, 0, 1, 0)):
        l1 += '{} {} '.format(' ' * c, s('_', v[i][0]))
        l2 += '{}{}{}'.format(s('|', v[i][5]), s('_', v[i][6]), s('|', v[i][1]))
        l2 += inter[i]
        l3 += '{}{}{}'.format(s('|', v[i][4]), s('_', v[i][3]), s('|', v[i][2]))
        l3 += inter[i]
    return '{}\n{}\n{}'.format(l1, l2, l3)

# dicionário com a entrada de 4 bits e o valor correspondente para acionar cada segmento
nb = {
    '0000': '1111110', # 0
    '0001': '0110000', # 1
    '0010': '1101101', # 2
    '0011': '1111001', # 3
    '0100': '0110011', # 4
    '0101': '1011011', # 5
    '0110': '0011111', # 6
    '0111': '1110000', # 7
    '1000': '1111111', # 8
    '1001': '1110011', # 9
    '1010': '1110111', # A
    '1011': '1100111', # P
    '1100': '1010101', # M
    '1111': '0000000', # vazio (quando for 24h)
}

#VARIAVEIS GLOBAIS
qfH = []
qfMin = []
qfSeg = []
am = []
flag = 0


#FUNÇÃO QUE RETORNA BINARIO DE 4 BYTES
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
    
    return bin_correto[4:8:1]


#CONVERTE BINARIO DE 4 BYTES PRAR DECIMAL
def conversor_bin_dec(vet_bin):

    dec = 0
    c = 3
    for num in vet_bin:
        if num == 1:
            dec += math.pow(2, c)
        c -= 1

    return int(dec)

#CONVERTE BINARIO DE 6 BYTES PARA BINARIO
def conversor_bin_decOther(vet_bin):
    dec = 0
    c = 5
    for num in vet_bin:
        if num == 1:
            dec += math.pow(2, c)
        c -= 1
    return int(dec)

def separador_de_bits(dec):

    dezena =  dec // 10
    unidade = dec % 10

    return dezena, unidade

#SEPARADOR DE BINARIO DAS HORAS
def divisionOfBinaryHour(horas):
    horasDec = conversor_bin_dec(horas)
    dezena, unidade = separador_de_bits(horasDec)
    binDezena = conversor_dec_bin(dezena)
    binUnidade = conversor_dec_bin(unidade)

    return binDezena, binUnidade

#DIVISOR DE BINARIO DOS SEGUNTOS E MINUTOS
def divisionOfBinary(horas):
    horasDec = conversor_bin_decOther(horas)
    dezena, unidade = separador_de_bits(horasDec)
    binDezena = conversor_dec_bin(dezena)
    binUnidade = conversor_dec_bin(unidade)

    return binDezena, binUnidade

#CONVERTE DECIMAL PARA BINARIO DE 6 BYTES
def conversor_dec_bin2(num):

    bin_invertido = []
    bin_correto = []

    while num > 0:

        bin_invertido.append(num % 2)
        num = num // 2

    while len(bin_invertido) < 8:

        bin_invertido.append(0)

    for i in range(len(bin_invertido) -1, -1, -1):

        bin_correto.append(bin_invertido[i])
    
    return bin_correto[2:8:1]


#RETORNA A HORA PARA FORMADO AM/PM
def retornoHoras(hora):
    global am

    #USADO PARA CONVERTER 0H PARA 12H
    if(hora == 0):
        am = '10101100'#AM
        return 12
    
    #USADO PARA ALTERAR AM/PM
    if(hora == 12):
        if(am == '10101100'):#AM
            am = '10111100' #PM
        else:
            am = '10101100'#AM
        return hora

    #USADO PARA FORMATAR FORMATO DE 24H PARA 12H
    if(hora >= 13):
        am = '10111100'
        if(hora == 13):
            hora = 1
        elif(hora == 14):
            hora = 2
        elif(hora == 15):
            hora = 3
        elif(hora == 16):
            hora = 4
        elif(hora == 17):
            hora = 5
        elif(hora == 18):
            hora = 6
        elif(hora == 19):
            hora = 7
        elif(hora == 20):
            hora = 8
        elif(hora == 21):
            hora = 9
        elif(hora == 22):
            hora = 10
        elif(hora == 23):
            hora = 11
    else:
        am = '10101100'#AM

    return hora

def contSegundos():
    global flag
    now = datetime.now()
    global qfSeg
    global am
    
    #N_FF == NUMERO DE FLIP FLOP'S
    n_ff = 6  # PODE MODIFICAR
    qfSeg, qa = [0] * (n_ff + 1), [0] * (n_ff + 1)

    # SEGUNDOS DO HORARIO ATUAL DO COMPUTADOR
    segundos = (conversor_dec_bin2(now.second))

    #SE FLAG == 0, ENTAO É SETADO SEGUNDOS DO HORARIO PEGO ACIMA
    if flag == 0: 
        pr = str(''.join(str(i) for i in segundos))
    else:
        pr = '000000'
    for i, p in enumerate(pr[-1::-1]):
        qfSeg[i] = qa[i] = int(p)
    
    #CLEAR
    cl = '111100' # PODE MODIFICAR

    #PEGANDO VALOR DO CLOCK INICIAL
    ck = int(pr, 2) * 2
    while True:
        try:
            if cl == ''.join([str(q) for q in qfSeg[-2::-1]]):
                for i in range(len(qfSeg)):
                    qfSeg[i] = qa[i] = 0
                ck = 0
                return

            flag = 1
             
            
            #SEPARANDO HORAS, MINUTOS E SEGUNDOS EM DEZENA E UNIDADE
            dezenaS, unidadeS = divisionOfBinary(qfSeg[-2::-1])
            dezenaM, unidadeM = divisionOfBinary(qfMin[-2::-1])
            dezenaH, unidadeH = divisionOfBinaryHour(qfH[-2::-1])

            
            #CONVERTENDO VALORES PEGOS PARA STRING
            srtDezenaS = str(''.join(str(i) for i in dezenaS))
            srtUnidadeS = str(''.join(str(i) for i in unidadeS))
            srtDezenaM = str(''.join(str(i) for i in dezenaM))
            srtUnidadeM = str(''.join(str(i) for i in unidadeM))
            srtDezenaH = str(''.join(str(i) for i in dezenaH))
            srtUnidadeH = str(''.join(str(i) for i in unidadeH))
            srtAM = str(''.join(str(i) for i in am))

            #CONCATENANDO STRING E PRINTANDO RESULTADO
            binario = srtDezenaH+srtUnidadeH+srtDezenaM+srtUnidadeM+srtDezenaS+srtUnidadeS+srtAM
            print("\n"*100)
            print(segmentos_7(binario))

            # 1/2 segundo em baixa e 1/2 segundo em alta
            sleep(0.5)
            
            qa[0] = ff_jk(ck=(ck % 2), j=1, k=1, qa=qa[0])
            for i in range(1, (n_ff + 1)):
                if (ck + 1) % (2 ** i) == 0:
                    qa[i] = ff_jk(ck=qfSeg[i - 1], j=1, k=1, qa=qa[i])
                    qfSeg[i - 1] = qa[i - 1]
            ck += 1
        except KeyboardInterrupt:
            break

def contMin():
    global qfMin
    global flag
    now = datetime.now()

    #N_FF == NUMERO DE FLIP FLOP'S
    n_ff = 6  # PODE MODIFICAR
    qfMin, qa = [0] * (n_ff + 1), [0] * (n_ff + 1)

    # MINUTOS DO HORARIO ATUAL DO COMPUTADOR
    minutos = conversor_dec_bin2(now.minute)

    #SE FLAG == 0, ENTAO É SETADO MINUTOS DO HORARIO PEGO ACIMA
    if flag == 0: 
        pr = str(''.join(str(i) for i in minutos))
    else:
        pr = '000000'
    for i, p in enumerate(pr[-1::-1]):
        qfMin[i] = qa[i] = int(p)


    #CLEAR
    cl = '111011' # PODE MODIFICAR

    #PEGANDO VALOR DO CLOCK INICIAL
    ck = int(pr, 2) * 2
    while True:
        try:
            contSegundos()
            for i in range(2):
                if cl == ''.join([str(q) for q in qfMin[-2::-1]]):
                    for i in range(len(qfMin)):
                        qfMin[i] = qa[i] = 0
                    ck = 0
                    return
                # 1/2 segundo em baixa e 1/2 segundo em alta
                qa[0] = ff_jk(ck=(ck % 2), j=1, k=1, qa=qa[0])
                for i in range(1, (n_ff + 1)):
                    if (ck + 1) % (2 ** i) == 0:
                        qa[i] = ff_jk(ck=qfMin[i - 1], j=1, k=1, qa=qa[i])
                        qfMin[i - 1] = qa[i - 1]
                ck += 1
        except KeyboardInterrupt:
            break

def dozehoras():
    global flag
    global qfH
    global am

    #N_FF == NUMERO DE FLIP FLOP'S
    n_ff = 4  # PODE MODIFICAR
    qfH, qa = [0] * (n_ff + 1), [0] * (n_ff + 1)

    # HORAS DO HORARIO ATUAL DO COMPUTADOR
    horas = retornoHoras(now.hour)
    horas = conversor_dec_bin(horas)

    #SE FLAG == 0, ENTAO É SETADO MINUTOS DO HORARIO PEGO ACIMA
    if flag == 0: 
        pr = str(''.join(str(i) for i in horas))
    else:
        pr = '0001'  # PODE MODIFICAR
    for i, p in enumerate(pr[-1::-1]):
        qfH[i] = qa[i] = int(p)

    #CLEAR
    cl = '1101' # PODE MODIFICAR

    #PEGANDO VALOR DO CLOCK INICIAL
    ck = int(pr, 2) * 2
    while True:
        try:
            contMin()
            
            for i in range(2):
                if cl == ''.join([str(q) for q in qfH[-2::-1]]):
                    for i in range(len(qfH)):
                        qfH[i] = qa[i] = 0
                    ck = 0
                    
                # 1/2 segundo em baixa e 1/2 segundo em alta
                qa[0] = ff_jk(ck=(ck % 2), j=1, k=1, qa=qa[0])
                for i in range(1, (n_ff + 1)):
                    if (ck + 1) % (2 ** i) == 0:
                        qa[i] = ff_jk(ck=qfH[i - 1], j=1, k=1, qa=qa[i])
                        qfH[i - 1] = qa[i - 1]
                ck += 1

            #CHAMEI FUNÇÃO PARA ALTERAR AM/PM
            horas = retornoHoras(conversor_bin_dec(qfH[-2::-1]))
        except KeyboardInterrupt:
            break


dozehoras()