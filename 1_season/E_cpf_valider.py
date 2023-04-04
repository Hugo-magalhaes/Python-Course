while True:
    cpf_orig = input('Informe um cpf:')
    cpf = cpf_orig[:-2]
    '''
# Parte para um cpf com ponto e traço
cpf = cpf.split('.')
cpf = ''.join(cpf)

num_cpf = []
for valor in cpf:
    if valor.isnumeric():
        num_cpf.append(int(valor))
    else:
        pass
# print(num_cpf)
    '''
    contagem = list(range(len(cpf)+1, 1, -1))
# print(contagem)
    multi = 0
    for valor, inverse in enumerate(contagem):
        # print(cpf[valor], inverse)
        multi += int(cpf[valor])*inverse

    multi = 11 - (multi % 11)
    multi = 0 if multi > 9 else multi
    multi = str(multi)
    cpf += multi
    # print(cpf)
    # print(multi)

    contagem = list(range(len(cpf)+1, 1, -1))
    multi1 = 0
    for valor, inverse in enumerate(contagem):
        # print(cpf[valor], inverse)
        multi1 += int(cpf[valor])*inverse

    multi1 = 11 - (multi1 % 11)
    multi1 = 0 if multi1 > 9 else multi1
    multi1 = str(multi1)
    cpf += multi1

    num_cpf_orig = ''
    for valor in cpf_orig:
        if valor.isnumeric():
            num_cpf_orig += str(valor)
        else:
            pass

    # print(cpf, num_cpf_orig)
    if cpf == num_cpf_orig:
        print('Cadastro concluído')
        break
    else:
        print(' CPF incorreto')
