def limpeza(cnpj):
    import re
    return re.sub(r'[^0-9]', '', cnpj)


def laco(init):
    contagem = []

    for i in range(init, 1, -1):
        contagem.append(i)
    for i in range(9, 1, -1):
        contagem.append(i)
    return contagem


def multiplicacao(cnpj, contador):
    cnpj = limpeza(cnpj)
    multi = 0
    for ind, inv in enumerate(contador):
        multi += int(cnpj[ind]) * inv

    valor = 11 - (multi % 11)
    valor = '0' if valor >= 9 else str(valor)
    cnpj += valor
    return cnpj


def conta(cnpj):
    cnpj = limpeza(cnpj)
    num_cnpj = cnpj[:-2]

    if len(num_cnpj) == 12:
        contador = laco(5)
        novo_cnpj = multiplicacao(num_cnpj, contador)
        contador = contador[1:]
        novo_cnpj = multiplicacao(novo_cnpj, contador)
        if novo_cnpj == cnpj:
            print('Cnpj Valido')
        else:
            print(f'Cnpj {novo_cnpj} não é igual ao cnpj inserido')
        return novo_cnpj
    else:
        print('Insira um cnpj valido')


def gera_digito(cnpj):

    if len(cnpj) == 12:
        contador = laco(5)
        novo_cnpj = multiplicacao(cnpj, contador)
        contador = contador[1:]
        novo_cnpj = multiplicacao(novo_cnpj, contador)
        return  novo_cnpj
    else:
        print('Insira um cnpj valido')


def gerador_cnpj():
    from random import randint
    cnpj = ''
    for i in range(8):
        cnpj += str(randint(0, 9))
    cnpj += '0001'
    cnpj = gera_digito(cnpj)
    return cnpj


def pontos(cnpj):
    cnpj = f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}'
    print(cnpj)


def pontua(cnpj):
    cnpj_p = ''
    for i, v in enumerate(cnpj):
        cnpj_p += v
        if i/1 == 1:
            cnpj_p += '.'
        elif i/4 == 1:
            cnpj_p += '.'
        elif i/7 == 1:
            cnpj_p += '/'
        elif i/11 == 1:
            cnpj_p += '-'
    print(cnpj_p)


def limpeza_lenta(cnpj):
    cnpj = cnpj.split('.')
    cnpj = ''.join(cnpj)
    cnpj = cnpj.split('/')
    cnpj = ''.join(cnpj)
    cnpj = cnpj.split('-')
    cnpj = ''.join(cnpj)
    return cnpj


def limpeza_meio(cnpj):
    cnpj = cnpj.replace('.', '')
    cnpj = cnpj.replace('/', '')
    cnpj = cnpj.replace('-', '')
    return cnpj
