try:
    a = 1
except NameError as erro:
    print('Erro de nomeação de variável')
except (IndexError, KeyError) as erro:
    print('Erro de indice')
except Exception as erro:
    print('Erro inesperado')
else:
    pass
finally:
    a = None

'Tratando erros em funções'


def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as error:
        print(error)
        raise


# Erro é recriado por causa do raise
try:
    print(divide(2, 0))
except ZeroDivisionError as erro:
    print(erro)


def divid(n1, n2):
    if n2 == 0:
        raise ValueError('n2 não pode ser 0')
    return n1/n2


try:
    print(divid(2, 0))
except ValueError as erro:
    print(erro)
