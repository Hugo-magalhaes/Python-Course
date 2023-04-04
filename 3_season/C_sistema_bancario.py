from abc import ABC, abstractmethod

# import datetime as dtt
# from enum import Enum


class Pessoa:
    def __init__(self, nome: str, age: int) -> None:
        self.nome = nome.capitalize()
        self.age = age

        @property
        def nome(self):
            return self._nome

        @nome.setter
        def nome(self, nome: str):
            self._nome = nome

        @property
        def age(self):
            return self._age

        @age.setter
        def age(self, age: int):
            self._age = age

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        attrs = f'({self.nome!r}, {self.age!r})'
        return f'{class_name}{attrs}'

    # ! Classe abstrata só existe se formos ter métodos abstratos


class Conta(ABC):
    AGENCIA = 3197
    CONTA = 28199
    BANCO = 'Goldbridge'

    def __init__(self, agencia: int, conta: int, saldo: float = 0) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abstractmethod
    def saque(self, valor: float) -> float: ...

    def autentica(self, msg: str = '') -> None:
        print(f'{msg}')
        print('--')

    def movimentacoes(self, msg: str = '') -> None:
        print(f'O seu saldo é R${self.saldo:.2f} {msg}')
        print('--')

    def _autenticao(self) -> None:
        # if self.banco != self.BANCO:
        #     self.autentica('Banco inválido')
        #     return

        if self.agencia != self.AGENCIA:
            self.autentica('Agência incorreta')
            return

        elif self.conta != self.CONTA:
            self.autentica('Essa conta está incorreta ou não existe')
            return

        else:
            self.autentica('Acesso concluído')
            return

    def deposito(self, valor: float) -> float:
        self._autenticao()
        self.saldo += valor
        self.movimentacoes(f'(DEPÓSITO REALIZADO R${valor})')
        return self.saldo


class ContaPoupanca(Conta):
    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo})'
        return f'{class_name}{attrs}'

    def saque(self, valor: float) -> float:
        self._autenticao()

        if self.saldo >= valor:
            self.saldo -= valor
            self.movimentacoes(f'(SAQUE REALIZADO R$({valor})')
            return self.saldo

        self.movimentacoes(f'(SAQUE NEGADO R$({valor})')
        return self.saldo


class ContaCorrente(Conta):
    def __init__(self, agencia: int, conta: int,
                 saldo: float = 0, limite: float = 0) -> None:
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r},' \
            f'{self.limite!r})'
        return f'{class_name}{attrs}'

    def saque(self, valor: float) -> float:

        juros = 0.5
        self._autenticao()

        if self.saldo >= valor:
            self.saldo -= valor
            self.movimentacoes(f'(SAQUE REALIZADO R$({valor})')
            return self.saldo

        if self.saldo + self.limite >= valor:
            resposta = input('''
                Você está pegando empréstimo, deseja continua? \n
                  [S]im ou [N]ão
                  ''')

            if resposta.upper() == 'S':
                self.saldo -= valor
                self._valor = valor*(1 + juros)
                self.movimentacoes(f'(SAQUE EMPRÉSTIMO REALIZADO R$({valor})')
                return self.saldo

        self.movimentacoes(f'(SAQUE NEGADO R${valor})')
        return self.saldo


class Cliente(Pessoa):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.conta: Conta | None = None

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        attrs = f'({self.nome!r}, {self.age!r})'
        return f'{class_name}{attrs}'


class Banco:
    def __init__(self, agencias: list[int] | None = None,
                 clientes: list[Pessoa] | None = None,
                 contas: list[Conta] | None = None) -> None:

        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        attrs = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r})'
        return f'{class_name}{attrs}'


if __name__ == '__main__':
    c1 = Cliente('Luiz', 30)
    c1.conta = ContaCorrente(3197, 28199, 0, 1)
    c1.conta.deposito(1)
    c1.conta.saque(1)
    c1.conta.saque(1)
    c1.conta.saque(1)
