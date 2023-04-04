from abc import ABC, abstractmethod


class AbstractFoo(ABC):
    def __init__(self, lista):
        self._lista = None
        self.lista = lista

    @property
    @abstractmethod
    def lista(self, lista): ...


class Foo(AbstractFoo):

    def __init__(self, lista):
        super().__init__(lista)

    @property
    def lista(self):
        return self._lista

    @lista.setter
    def lista(self, lista):
        self._lista = lista


l = Foo(lista='nenhuma')
print(l.lista)
