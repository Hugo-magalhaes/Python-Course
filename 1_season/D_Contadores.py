contador = input('Coloque um número: ')

while True:
    if contador.isnumeric():
        lista = list(range(int(contador), -1, -1))
        break
    else:
        contador = input('Coloque um número: ')

for valor, inverse in enumerate(lista):
    print(valor, inverse)