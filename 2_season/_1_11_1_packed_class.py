pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

(a1, a2), (b1, b2) = pessoa.items()
print(a1, a2, '\n',
      b1, b2)

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

infos = {**dados_pessoa,
         **pessoa,
         'chave': 1}


def argumentos_nomeados(*args, **kwargs):
    print('Nao nomeados', args)

    for chave, valor in kwargs.items():
        print(chave, valor)


argumentos_nomeados(**pessoa)
