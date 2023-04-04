#  Dataclasses - syntex sugar
#  Dataclasses determinam repr e equal instantaneamente

from dataclasses import asdict, astuple, dataclass, field


# @dataclass(init=False) # Assim você determina seu próprio init
@dataclass(order=True)
class Pessoa:
    nome: str
    sobrenome: str
    idade: int = 0
    enderecos: list[str] = field(default_factory=list)

    def __post_init__(self):
        self.nome_completo = f'{self.nome} {self.sobrenome}'

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

    @nome_completo.setter
    def nome_completo(self, valor):
        nome, *sobrenome = valor.split()
        self.nome = nome
        self.sobrenome = ' '.join(sobrenome)


if __name__ == '__main__':
    p1 = Pessoa('Hugo', 'Magalhães')
    p = [Pessoa('Hugo', 'Magalhães'), Pessoa(
        'Miguel', 'Chichorro'), Pessoa('Geovana', 'Vieira')]
    ordem = sorted(p)
    print(ordem)
    # -- Se você quiser pode desativar, e criar seu prórpio order
    print()
    ordem_own = sorted(p, key=lambda p: p.sobrenome)
    print(ordem_own)
    print()
    print(asdict(p1))
    print()
    print(astuple(p1))
    # print(p1.nome_completo)
    # p1.nome_completo = 'Hugo Magalhães Martins Júnior'
    # print(p1.nome_completo)
