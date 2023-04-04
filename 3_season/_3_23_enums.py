# Vamos falar sobre enumerações e a supercalsse Enum
import enum

# Direcoes = enum.Enum('Direçoes', ['ESQUERDA', 'DIREITA'])
# print(Direcoes(1))
# print(Direcoes['DIREITA'])
# print(Direcoes.DIREITA)


class Direcoes(enum.Enum):
    ESQUERDA = enum.auto()
    DIREITA = enum.auto()
    CIMA = enum.auto()
    BAIXO = enum.auto()


def mover(direcao: Direcoes):
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção não encontrada')
    print(f'Movendo para {direcao.name}')


mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
