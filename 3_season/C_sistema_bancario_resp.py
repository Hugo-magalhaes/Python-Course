from abc import ABC, abstractmethod


class Pessoa:
    def __init__(self, nome: str, age: int) -> None:
        self.nome = nome.capitalize()
        self.age = age

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        attrs = f'({self.nome!r}, {self.age!r})'
        return f'{class_name}{attrs}'

    # ! Classe abstrata só existe se formos ter métodos abstratos


class Conta(ABC):
    def __init__(self, agencia, conta, saldo=0) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abstractmethod
    def sacar(self, valor): ...

    def depositar(self, valor):
        self.saldo += valor
        self.detalhes(f'(DEPÓSITO R${valor:.2f})')

    def detalhes(self, msg=''):
        print(f'O seu saldo é R${self.saldo:.2f} {msg}')
        print('--')


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            self.detalhes(f'(SAQUE R${valor:.2f})')
            return self.saldo

        print(f'Saldo R${self.saldo:.2f} insuficiente (SAQUE NEGADO)')


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo=0, limite=0) -> None:
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            self.detalhes(f'(SAQUE R${valor:.2f})')
            return self.saldo

        elif valor <= self.saldo + self.limite:
            self.saldo -= valor
            self.detalhes(f'(SAQUE EMPRÉSTIMO R${valor:.2f})')
            return self.saldo

        print(
            f'Saldo R${self.saldo:.2f} e limite não utilizado'
            f'R${self.limite:.2f} insuficiente (SAQUE NEGADO)')


class Cliente(Pessoa):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.conta: Conta | None = None

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        attrs = f'({self.nome!r}, {self.age!r})'
        return f'{class_name}{attrs}'


class Banco:
    def __init__(
        self,
        agencias: list[int] | None = None,
        clientes: list[Pessoa] | None = None,
        contas: list[Conta] | None = None,
    ):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def _checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            print('_checa_agencia', True)
            return True
        print('_checa_agencia', False)
        return False

    def _checa_cliente(self, cliente):
        if cliente in self.clientes:
            print('_checa_cliente', True)
            return True
        print('_checa_cliente', False)
        return False

    def _checa_conta(self, conta):
        if conta in self.contas:
            print('_checa_conta', True)
            return True
        print('_checa_conta', False)
        return False

    def _checa_se_conta_e_do_cliente(self, cliente, conta):
        if conta is cliente.conta:
            print('_checa_se_conta_e_do_cliente', True)
            return True
        print('_checa_se_conta_e_do_cliente', False)
        return False

    def autenticar(self, cliente: Pessoa, conta: Conta):
        return self._checa_agencia(conta) and \
            self._checa_cliente(cliente) and \
            self._checa_conta(conta) and \
            self._checa_se_conta_e_do_cliente(cliente, conta)

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r})'
        return f'{class_name}{attrs}'


if __name__ == '__main__':
    # cp = ContaPoupanca(111, 222, 0)
    # cp.depositar(1)
    # cp.sacar(1)
    # cp.sacar(1)
    cc = ContaCorrente(111, 222, limite=1)
    cc.depositar(1)
    cc.sacar(1)
    cc.sacar(1)
    cc.sacar(1)
