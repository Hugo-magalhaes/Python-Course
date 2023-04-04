from functools import reduce
from dados import lista, pessoas, produtos

#            acumulador, item           inicia
soma = reduce(lambda ac, i: ac+i, lista, 0)

# Mesma coisa
acumuladora = 0

for item in lista:
    acumuladora += item

print(soma)
print(acumuladora)


sacola = reduce(lambda ac, i: ac+i['preço'], produtos, 0)

print(sacola)

media = reduce(lambda ac, i: ac+i['idade'], pessoas, 0)

print(media/len(pessoas))
