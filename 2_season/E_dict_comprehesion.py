carrinho = [('Produto 1', 20),
            ('Produto 2', 30),
            ('Produto 3', 50)]

total = [x[1] for x in carrinho]

total1 = sum([float(y) for x, y in carrinho])

print(total1)
