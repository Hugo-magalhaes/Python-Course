from collections.abc import Callable

soma_inteiros = Callable[[int, int], int]


def executa(func: soma_inteiros, a: int, b: int) -> float:
    return func(a, b)


def soma(x: int, y: int) -> int:
    return x+y


def soma2(x: float, y: float) -> float:
    return x+y


executa(soma, 1, 2)
executa(soma2, 1, 2)
