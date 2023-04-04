# Determinando o motivo de getter e setter
#  Getter(property) = Obter um valor -- Pode exister sozinho
# Setter(property.setter) = Configura um valor -- Depende do Getter
#  Ao utilizar um getter(property), não podemos chamar a função(), só um atributo.atribut
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = round(self.preco * (1 - (percentual / 100)), 2)

    # Getter
    @property
    def preco(self):
        return self._preco

    # Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()


p1 = Produto('CAMISTA', 'R$50')
p2 = Produto('caneca', 'R$50.00')
p3 = Produto('rODO', 50)

p1.desconto(10)
p2.desconto(30)
print(p1.nome, p1.preco)
print(p2.nome, p2.preco)
print(p3.nome, p3.preco)