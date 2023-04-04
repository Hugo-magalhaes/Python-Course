lis1 = [1, 2, 3]
lis2 = [2, 3, 4]

# Utilizado para estender uma lista
lis1[0] = 0
lis1.extend(lis2)
lis3 = lis1 + lis2

# Append adiciona itens na lista
lis1.append(lis2)

# Utilizado para inserir em qualquer lugar da list//a
lis1.insert(0, 'primeiro')

# Remove o último item da lista
lis1.pop()

# apagar vários valores
lis4 = [1, 2, 3, 4, 5, 6, 7]
del (lis4[2:5])

# range e list são iteráveis
# Iteração é o objeto que pode acessar qualquer elemento dele

l1 = ['banana', True, 10, -20.5]
# Os dois pontos representam a separação de início, fim e passo
print(l1[::-2])

for valor in l1:
    print(f' O tipo de {valor} é {type(valor)}')

l2 = list(range(1, 10, 2))
