import json


class Pessoa:

    def __init__(self, nome, sobrenome, idade):

        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

        # with open(f'{self.nome}_arquivo.json', 'w', encoding='utf8') as arquivo:
        #     json.dump(self.__dict__, arquivo, indent=2)

    def salvar_arquivo(caminho='dados.json', ):
        with open(caminho, 'w', encoding='utf8') as arquivo:
            json.dump(pessoas, arquivo, ensure_ascii=False, indent=2)

    if __name__ == '__main__':
        salvar_arquivo()


p1 = Pessoa('Hugo', 'Magalhães', 22)
p2 = Pessoa('Maria', 'Helena', 30)
p3 = Pessoa('Miguel', 'Chichoro', 18)
pessoas = [p1.__dict__, p2.__dict__, p3.__dict__]


with open('dados.json', 'r', encoding='utf8') as arquivo:
    pessoas = json.load(arquivo)
    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])
    p3 = Pessoa(**pessoas[2])
    print(p1.nome, p2.nome, p3.nome, sep='\n')


# with open('Hugo_arquivo.json', 'r', encoding='utf8') as arquivo:
#     pessoa = json.load(arquivo)
#     p1 = Pessoa(**pessoa)
#     print(p1.nome, p1.sobrenome, p1.idade)
