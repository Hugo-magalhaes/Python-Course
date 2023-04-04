from dados import produtos, pessoas, lista


lista1 = filter(lambda x: x > 5, lista)
lista2 = [x for x in lista if x > 5]


preco = filter(lambda p: p['preço'] > 50, produtos)

print(list(preco))

print()
idade = filter(lambda i: i['idade'] > 21, pessoas)

print(list(idade))

