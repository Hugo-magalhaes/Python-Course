from time import time


# Decorador
def master(funcao):
    def slave(*args, **kwargs):
        print('Trabalhando...')
        funcao(*args, **kwargs)

    return slave


# Decorado
@master
def fala_oi():
    print('Sendo de corada')


@master
def mando(msg):
    print(msg)


mando('Modificando a função')


def tempo(funcao):
    def calc_tempo(*args, **kwargs):
        start = time()
        funcao(*args, **kwargs)
        end = time()
        tempo_t = round((end - start) * 1000, 2)
        print(f'\n A função {funcao.__name__} leva {tempo_t} ms para executar')
        return tempo_t

    return calc_tempo


@tempo
def morte():
    for i in range(100):
        print(i, end='')


morte()
