from time import sleep


def p_nand_2(a, b):
    return int(not(a and b))

def p_nand_3(a, b, c):
    return int(not(a and b and c))

def p_not(a):
    return int(not(a))

def ff_jk(ck=1, j=1, k=1, qa=0, test=0):
    qa1, qa2 = qa, p_not(qa)
    qf1, qf2 = qa1, qa2
    while True:
        s1 = p_nand_3(j, ck, qa2)
        s2 = p_nand_3(k, ck, qa1)
        qf1 = p_nand_2(s1, qf2)
        qf2 = p_nand_2(s2, qf1)
        if qf1 != qf2:
            return qf1
        elif test:
            print('Atualização:', qf1, qf2)


# # TESTES DO FLIP-FLOP JK
# print('Saída:', ff_jk(ck=0, j=1, k=1, qa=0, test=1))
# print('Saída:', ff_jk(ck=0, j=1, k=1, qa=1, test=1))
# print('Saída:', ff_jk(ck=1, j=1, k=1, qa=0, test=1))
# print('Saída:', ff_jk(ck=1, j=1, k=1, qa=1, test=1))
# print()
# print('Saída:', ff_jk(ck=0, j=1, k=1, qa=0, test=1))
# print('Saída:', ff_jk(ck=0, j=1, k=1, qa=1, test=1))
# print('Saída:', ff_jk(ck=1, j=1, k=1, qa=0, test=1))
# print('Saída:', ff_jk(ck=1, j=1, k=1, qa=1, test=1))


# # 1ª FORMA DE FAZER com FOR's aninhados
# qf = [0, 0, 0, 0]
# qa = [0, 0, 0, 0]
# while True:
#     for _ in range(2):
#         for _ in range(2):
#             for ck in range(2):
#                 print('\n' * 50)
#                 print(qf[::-1])
#                 qa[0] = ff_jk(ck=ck, j=1, k=1, qa=qf[0])
#                 # 1/2 segundo em baixa e 1/2 segundo em alta
#                 sleep(0.5)
#             qa[1] = ff_jk(ck=qf[0], j=1, k=1, qa=qf[1])
#             qf[0] = qa[0]
#         qa[2] = ff_jk(ck=qf[1], j=1, k=1, qa=qf[2])
#         qf[1] = qa[1]
#     qf[3] = ff_jk(ck=qf[2], j=1, k=1, qa=qf[3])
#     qf[2] = qa[2]


# # 2ª FORMA DE FAZER com IF's comparando as potências e adicionando "PRESET"
# # e "CLEAR" no flip-flop (mudar variáqveis para testar)
# n_ff = 4  # PODE MODIFICAR
# qf, qa = [0] * (n_ff + 1), [0] * (n_ff + 1)
# # setando valor de "preset" (valor = 6 [0110])
# pr = '0110'  # PODE MODIFICAR
# for i, p in enumerate(pr[-1::-1]):
#     qf[i] = qa[i] = int(p)
# # setando valor de "clear" (valor = 12 [1100], zera em 13 [1101])
# cl = '1101' # PODE MODIFICAR
# # funcionamento ...
# ck = int(pr, 2) * 2
# while True:
#     try:
#         if cl == ''.join([str(q) for q in qf[-2::-1]]):
#             for i in range(len(qf)):
#                 qf[i] = qa[i] = 0
#             ck = 0
#         print('\n' * 50)
#         print(qf[-2::-1])
#         # 1/2 segundo em baixa e 1/2 segundo em alta
#         sleep(0.5)
#         if (ck + 1) % 2 == 0:
#             qa[1] = ff_jk(ck=qf[0], j=1, k=1, qa=qf[1])
#             qf[0] = qa[0]
#         if (ck + 1) % 4 == 0:
#             qa[2] = ff_jk(ck=qf[1], j=1, k=1, qa=qf[2])
#             qf[1] = qa[1]
#         if (ck + 1) % 8 == 0:
#             qf[3] = ff_jk(ck=qf[2], j=1, k=1, qa=qf[3])
#             qf[2] = qa[2]
#     except KeyboardInterrupt:
#         break

def contSegundos():
    # 3ª FORMA DE FAZER enxugando a 2ª forma
    n_ff = 6  # PODE MODIFICAR
    qf, qa = [0] * (n_ff + 1), [0] * (n_ff + 1)
    # setando valor de "preset" (valor = 6 [0110])
    pr = '000000'  # PODE MODIFICAR
    for i, p in enumerate(pr[-1::-1]):
        qf[i] = qa[i] = int(p)
    # setando valor de "clear" (valor = 12 [1100], zera em 13 [1101])
    cl = '111100' # PODE MODIFICAR
    # funcionamento ...
    ck = int(pr, 2) * 2
    while True:
        try:
            if cl == ''.join([str(q) for q in qf[-2::-1]]):
                for i in range(len(qf)):
                    qf[i] = qa[i] = 0
                ck = 0
            print('\n')
            print(qf[-2::-1],  "SEGUNDOS")
            # 1/2 segundo em baixa e 1/2 segundo em alta
            sleep(0.5)
            qa[0] = ff_jk(ck=(ck % 2), j=1, k=1, qa=qa[0])
            for i in range(1, (n_ff + 1)):
                if (ck + 1) % (2 ** i) == 0:
                    qa[i] = ff_jk(ck=qf[i - 1], j=1, k=1, qa=qa[i])
                    qf[i - 1] = qa[i - 1]
            ck += 1
        except KeyboardInterrupt:
            break


def contMin():
    # 3ª FORMA DE FAZER enxugando a 2ª forma
    n_ff = 6  # PODE MODIFICAR
    qf, qa = [0] * (n_ff + 1), [0] * (n_ff + 1)
    # setando valor de "preset" (valor = 6 [0110])
    pr = '000000'  # PODE MODIFICAR
    for i, p in enumerate(pr[-1::-1]):
        qf[i] = qa[i] = int(p)
    # setando valor de "clear" (valor = 12 [1100], zera em 13 [1101])
    cl = '111100' # PODE MODIFICAR
    # funcionamento ...
    ck = int(pr, 2) * 2
    while True:
        try:
            if cl == ''.join([str(q) for q in qf[-2::-1]]):
                for i in range(len(qf)):
                    qf[i] = qa[i] = 0
                ck = 0
            print('\n')
            print(qf[-2::-1],  "MINUTOS")
            # 1/2 segundo em baixa e 1/2 segundo em alta
            sleep(0.5)
            qa[0] = ff_jk(ck=(ck % 2), j=1, k=1, qa=qa[0])
            contSegundos()
            for i in range(1, (n_ff + 1)):
                if (ck + 1) % (2 ** i) == 0:
                    qa[i] = ff_jk(ck=qf[i - 1], j=1, k=1, qa=qa[i])
                    qf[i - 1] = qa[i - 1]
            ck += 1
        except KeyboardInterrupt:
            break

def dozehoras():
    # 3ª FORMA DE FAZER enxugando a 2ª forma
    n_ff = 4  # PODE MODIFICAR
    qf, qa = [0] * (n_ff + 1), [0] * (n_ff + 1)
    # setando valor de "preset" (valor = 6 [0110])
    pr = '0000'  # PODE MODIFICAR
    for i, p in enumerate(pr[-1::-1]):
        qf[i] = qa[i] = int(p)
    # setando valor de "clear" (valor = 12 [1100], zera em 13 [1101])
    cl = '1101' # PODE MODIFICAR
    # funcionamento ...
    ck = int(pr, 2) * 2
    while True:
        try:
            if cl == ''.join([str(q) for q in qf[-2::-1]]):
                for i in range(len(qf)):
                    qf[i] = qa[i] = 0
                ck = 0
            print('\n')
            print(qf[-2::-1],  "HORAS")
            # 1/2 segundo em baixa e 1/2 segundo em alta
            sleep(0.5)
            contMin()
            qa[0] = ff_jk(ck=(ck % 2), j=1, k=1, qa=qa[0])
            for i in range(1, (n_ff + 1)):
                if (ck + 1) % (2 ** i) == 0:
                    qa[i] = ff_jk(ck=qf[i - 1], j=1, k=1, qa=qa[i])
                    qf[i - 1] = qa[i - 1]
            ck += 1
        except KeyboardInterrupt:
            break

dozehoras()