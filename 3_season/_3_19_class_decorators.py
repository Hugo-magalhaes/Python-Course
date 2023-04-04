def adiciona_repr(cls):
    def meu_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        return f'{class_name} {class_dict}'
    cls.__repr__ = meu_repr
    return cls


def meu_palneta(metodo):
    def interno(self, *args, **kwargs):
        resultado = metodo(self, *args, **kwargs)

        if 'Terra' in resultado:
            return 'O planeta é casa'
        return resultado
    return interno


@adiciona_repr
class Time:
    def __init__(self, name) -> None:
        self.name = name


@adiciona_repr
class Planeta:
    def __init__(self, name) -> None:
        self.name = name

    @meu_palneta
    def falar_nome(self, name):
        return f'O planeta é {self.name}'


class Multiplicard:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)


@Multiplicard
def soma1(x, y):
    return x+y


class Multiplicar:
    def __init__(self) -> None:
        ...

    def __call__(self, func):
        def interna(*args, **kwargs):
            return func(*args, **kwargs)
        return interna


@Multiplicar()
def soma(x, y):
    return x+y


meu = Planeta('Terra')
meu1 = Planeta('Marte')

somu = print(soma1(2, 2))
somu = print(soma(2, 2))
