def repr_my(self):
    return f'{type(self).__name__}({self.__dict__})'


class Meta(type):
    def __new__(mcs, name, bases, dct):
        print('Meu metaclass new')
        cls = super().__new__(mcs, name, bases, dct)
        cls.attr = 1234
        cls.__repr__ = repr_my

        if 'falar' not in cls.__dict__ or \
                not callable(cls.__dict__['falar']):
            raise NotImplementedError('Implemente o método falar')
        return cls

    def __call__(cls, *args, **kwargs):
        instancia = super().__call__(*args, **kwargs)
        print(instancia.__dict__)
        return instancia


class Pessoa(metaclass=Meta):
    def __new__(cls, *args, **kwargs):
        print('Meu new class')
        instancia = super().__new__(cls)
        return instancia

    def __init__(self, name) -> None:
        self.name = name

    def falar():
        ...
