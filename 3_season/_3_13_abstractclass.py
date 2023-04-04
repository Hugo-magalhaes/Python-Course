from abc import ABC

#  Toda classe abstrata deve receber ABC - Abstract Base Class


class AbstractFoo(ABC):
    def _foo(self, msg): ...  # Método abstrato nunca tem corpo

    def foo_error(self, msg):
        return self._foo(f'"Error": {msg}')


class Foo(AbstractFoo):
    def _foo(self, msg):
        print(f'{msg} sou {self.__class__.__name__}')


l = Foo()
l.foo_error('oi')
