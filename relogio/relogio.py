from time import sleep
import math
from datetime import datetime
now = datetime.now()
import os

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
qf_h = []
qf_min = []
qf_seg = []
am_pm = []
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
def divisao_de_hora_binaria(horas):
    horas_dec = conversor_bin_dec(horas)
    dezena, unidade = separador_de_bits(horas_dec)
    bin_dezena = conversor_dec_bin(dezena)
    bin_unidade = conversor_dec_bin(unidade)

    return bin_dezena, bin_unidade

#DIVISOR DE BINARIO DOS SEGUNTOS E MINUTOS
def divisao_de_binario(horas):
    horas_dec = conversor_bin_decOther(horas)
    dezena, unidade = separador_de_bits(horas_dec)
    bin_dezena = conversor_dec_bin(dezena)
    bin_unidade = conversor_dec_bin(unidade)

    return bin_dezena, bin_unidade

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


#RETORNA A HORA PARA FORMADO am_pm/PM
def retorno_horas(hora):
    global am_pm

    #USADO PARA CONVERTER 0H PARA 12H
    if(hora == 0):
        am_pm = '10101100'#am_pm
        return 12
    
    #USADO PARA ALTERAR am_pm/PM
    if(hora == 12):
        if(am_pm == '10101100'):#am_pm
            am_pm = '10111100' #PM
        else:
            am_pm = '10101100'#am_pm
        return hora

    #USADO PARA FORMATAR FORMATO DE 24H PARA 12H
    if(hora >= 13):
        am_pm = '10111100'
        return hora-12
    else:
        am_pm = '10101100'#am_pm

    return hora

def cont_segundos():
    global flag
    now = datetime.now()
    global qf_seg
    global am_pm
    
    #N_FF == NUMERO DE FLIP FLOP'S
    n_ff = 6  # PODE MODIFICAR
    qf_seg, qa = [0] * (n_ff + 1), [0] * (n_ff + 1)

    # SEGUNDOS DO HORARIO ATUAL DO COMPUTADOR
    segundos = (conversor_dec_bin2(now.second))

    #SE FLAG == 0, ENTAO É SETADO SEGUNDOS DO HORARIO PEGO ACIMA
    if flag == 0: 
        pr = str(''.join(str(i) for i in segundos))
    else:
        pr = '000000'
    for i, p in enumerate(pr[-1::-1]):
        qf_seg[i] = qa[i] = int(p)
    
    #CLEAR
    cl = '111100' # PODE MODIFICAR

    #PEGANDO VALOR DO CLOCK INICIAL
    ck = int(pr, 2) * 2
    while True:
        try:
            if cl == ''.join([str(q) for q in qf_seg[5::-1]]):
                for i in range(len(qf_seg)):
                    qf_seg[i] = qa[i] = 0
                ck = 0
                return

            flag = 1
             
            
            #SEPARANDO HORAS, MINUTOS E SEGUNDOS EM DEZENA E UNIDADE
            #EXPLICAÇÃO PARA [5::-1] = [START:END:STEP]
            dezena_s, unidade_s = divisao_de_binario(qf_seg[5::-1])
            dezena_m, unidade_m = divisao_de_binario(qf_min[5::-1])
            dezena_h, unidade_h = divisao_de_hora_binaria(qf_h[3::-1])

            
            #CONVERTENDO VALORES PEGOS PARA STRING
            srt_dezena_s = str(''.join(str(i) for i in dezena_s))
            srt_unidade_s = str(''.join(str(i) for i in unidade_s))
            srt_dezena_m = str(''.join(str(i) for i in dezena_m))
            srt_unidade_m = str(''.join(str(i) for i in unidade_m))
            srt_dezena_h = str(''.join(str(i) for i in dezena_h))
            srt_unidade_h = str(''.join(str(i) for i in unidade_h))
            str_am_pm = str(''.join(str(i) for i in am_pm))

            #CONCATENANDO STRING E PRINTANDO RESULTADO
            binario = srt_dezena_h+srt_unidade_h+srt_dezena_m+srt_unidade_m+srt_dezena_s+srt_unidade_s+str_am_pm
            if (os.name == 'nt'): 
                os.system('cls')
            elif (os.name =='posix'):
                 os.system('clear')
            else: 
                print('\n'*120)
            # print("\n"*100)
            print(segmentos_7(binario))

            # 1/2 segundo em baixa e 1/2 segundo em alta
            sleep(0.5)
            
            qa[0] = ff_jk(ck=(ck % 2), j=1, k=1, qa=qa[0])
            for i in range(1, (n_ff + 1)):
                if (ck + 1) % (2 ** i) == 0:
                    qa[i] = ff_jk(ck=qf_seg[i - 1], j=1, k=1, qa=qa[i])
                    qf_seg[i - 1] = qa[i - 1]
            ck += 1
        except KeyboardInterrupt:
            break

def cont_min():
    global qf_min
    global flag
    now = datetime.now()

    #N_FF == NUMERO DE FLIP FLOP'S
    n_ff = 6  # PODE MODIFICAR
    qf_min, qa = [0] * (n_ff + 1), [0] * (n_ff + 1)

    # MINUTOS DO HORARIO ATUAL DO COMPUTADOR
    minutos = conversor_dec_bin2(now.minute)

    #SE FLAG == 0, ENTAO É SETADO MINUTOS DO HORARIO PEGO ACIMA
    if flag == 0: 
        pr = str(''.join(str(i) for i in minutos))
    else:
        pr = '000000'
    for i, p in enumerate(pr[-1::-1]):
        qf_min[i] = qa[i] = int(p)


    #CLEAR
    cl = '111011' # PODE MODIFICAR

    #PEGANDO VALOR DO CLOCK INICIAL
    ck = int(pr, 2) * 2
    while True:
        try:
            cont_segundos()
            for i in range(2):
                if cl == ''.join([str(q) for q in qf_min[5::-1]]):
                    for i in range(len(qf_min)):
                        qf_min[i] = qa[i] = 0
                    ck = 0
                    return
                # 1/2 segundo em baixa e 1/2 segundo em alta
                qa[0] = ff_jk(ck=(ck % 2), j=1, k=1, qa=qa[0])
                for i in range(1, (n_ff + 1)):
                    if (ck + 1) % (2 ** i) == 0:
                        qa[i] = ff_jk(ck=qf_min[i - 1], j=1, k=1, qa=qa[i])
                        qf_min[i - 1] = qa[i - 1]
                ck += 1
        except KeyboardInterrupt:
            break

def doze_horas():
    global flag
    global qf_h
    global am_pm

    #N_FF == NUMERO DE FLIP FLOP'S
    n_ff = 4  # PODE MODIFICAR
    qf_h, qa = [0] * (n_ff + 1), [0] * (n_ff + 1)

    # HORAS DO HORARIO ATUAL DO COMPUTADOR
    horas = retorno_horas(now.hour)
    horas = conversor_dec_bin(horas)

    #SE FLAG == 0, ENTAO É SETADO MINUTOS DO HORARIO PEGO ACIMA
    if flag == 0: 
        pr = str(''.join(str(i) for i in horas))
    else:
        pr = '0001'  # PODE MODIFICAR
    for i, p in enumerate(pr[-1::-1]):
        qf_h[i] = qa[i] = int(p)

    #CLEAR
    cl = '1101' # PODE MODIFICAR

    #PEGANDO VALOR DO CLOCK INICIAL
    ck = int(pr, 2) * 2
    while True:
        try:
            cont_min()
            
            for i in range(2):
                if cl == ''.join([str(q) for q in qf_h[3::-1]]):
                    for i in range(len(qf_h)):
                        qf_h[i] = qa[i] = 0
                    ck = 0
                    
                # 1/2 segundo em baixa e 1/2 segundo em alta
                qa[0] = ff_jk(ck=(ck % 2), j=1, k=1, qa=qa[0])
                for i in range(1, (n_ff + 1)):
                    if (ck + 1) % (2 ** i) == 0:
                        qa[i] = ff_jk(ck=qf_h[i - 1], j=1, k=1, qa=qa[i])
                        qf_h[i - 1] = qa[i - 1]
                ck += 1

            #CHam_pmEI FUNÇÃO PARA ALTERAR am_pm/PM
            horas = retorno_horas(conversor_bin_dec(qf_h[-2::-1]))
        except KeyboardInterrupt:
            break


doze_horas()