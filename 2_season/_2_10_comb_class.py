from itertools import combinations, permutations, product

pessoa = ['Luiz', 'Hugo', 'Miguel', 'Geovana']

# Combinanção não considera a ordem
for grupo in combinations(pessoa, 2):
    print(grupo)

print()

# Permutação considera todas as formas
for grupo in permutations(pessoa, 2):
    print(grupo)

print()

for grupo in product(pessoa, repeat=2):
    print(grupo)

