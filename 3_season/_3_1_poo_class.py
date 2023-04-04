from datetime import datetime
from random import randint


class Pessoa:
    ano = int(datetime.strftime(datetime.now(), '%Y'))

    # A variavel self representa a variavel que você definiu no seu código ao chamar a classe Personagem
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar, ele está comendo')
            return

        if self.falando:
            print(f'{self.nome} já está falando')
            return

        print(f'{self.nome} está falando de {assunto}')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando nada')
            return

        print(f'{self.nome} parou de falar')
        self.falando = False

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo')
            return

        if self.falando:
            print(f'{self.nome} está falando agora')
            return

        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo')
            return

        print(f'{self.nome} parou de comer')
        self.comendo = False

    def ano_nascimento(self):
        return self.ano - self.idade

    # Quando necessário algo em toda a classe
    @classmethod
    def por_ano(cls, nome, ano_nascimento):
        idade = cls.ano - ano_nascimento
        return cls(nome, idade)

    @staticmethod
    def gera_id():
        id_pes = randint(10000, 19999)
        return id_pes


p1 = Pessoa('Hugo', 21)

p1.comer('Maçã')
p1.comer('Bolo')
p1.parar_comer()
p1.falar('Python')
p1.comer('Bolo')
p1.parar_falar()
p1.parar_falar()
print(p1.ano_nascimento())

# Variável de classe
print(Pessoa.ano)

# Método de classe por ano
print(p1.idade)
p2 = Pessoa.por_ano('Hugo', 2000)
