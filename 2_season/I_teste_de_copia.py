import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
print(*produtos, sep='\n')
print('\n')
# ! ** Representa os argumentos nomeados da função
novos_produtos = [
    {**x, 'preco': round(x['preco']*1.1, 2)}
    for x in copy.deepcopy(produtos)
]
print(*novos_produtos, sep='\n')
print('\n')

prod_by_name = sorted(copy.deepcopy(novos_produtos),
                      key=lambda item: item['nome'])
print(*prod_by_name, sep='\n')
print('\n')

prod_by_price = copy.deepcopy(prod_by_name)
prod_by_price.sort(key=lambda item: item['preco'])
print(*prod_by_price, sep='\n')
