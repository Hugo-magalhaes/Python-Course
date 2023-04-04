# Tem o ponto porque matplotlib é a pasta raiz, e o pyplot é a subpasta
import sys
import importlib
# ! Essa forma abaixo você está abrindo uma pasta
# ! Você só pode importar um programa dessa pasta
# ! Se você tiver no 'import'
# from module_package.modulo import modulo_espeficio
# ? Para que o package se comporte como modulo
# ? É preciso criar um arquivo __init.py dentro dele


def divide(n1, n2, formata=False):
    if format:
        return round(n1 / n2, 2)
    else:
        return n1 / n2


def multiplica(n1, n2):
    return n1 * n2


# Dessa forma este código pode ser importado sem rodar todas as funções
if __name__ == '__main__':
    print(multiplica(2, 3))
    print(divide(2, 3))


print(__name__)
# sys.path.append('/Resto/do/caminho')
print(*sys.path, sep='\n')

for i in range(10):
    importlib.reload(sys)

# !Você pode fazer um arquivo dentro da pasta de modulos
# -- Chamado __all__ = [ Aqui dentro vai str dos nomes
# --                   dos modulos]
# ? Dessa forma você permite quais modulos serão utilizáveis
