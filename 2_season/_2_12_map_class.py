from dados import produtos, lista

lista_mu = map(lambda x: x * 2, lista)  # Mesma coisa
l_m = [x * 2 for x in lista]

preco = map(lambda p: round(p['preço'] * 1.1, 2), produtos)


# print(list(preco))  # Dessa forma não altera os valores do dict original


def high_price(prd):
    prd['preço'] = round(prd['preço'] * 1.5, 2)
    return prd


product = map(high_price, produtos)

for valor in product:
    print(valor)
