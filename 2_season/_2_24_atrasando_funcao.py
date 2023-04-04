def soma(x, y):
    return x+y


def multiplica(x, y):
    return x*y

#  Dessa forma armazena os atributos funcao e x e aguarda o y


def cria_funca(funcao, x):
    def interno(y):
        return funcao(x, y)
    return interno


somaa = cria_funca(soma, 4)
multiplicaa = cria_funca(multiplica, 10)

print(somaa(6))
print(multiplicaa(10))
