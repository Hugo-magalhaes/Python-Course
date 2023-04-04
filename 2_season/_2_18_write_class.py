# https://docs.python.org/3/library/functions.html#open

from os import remove
import json

#  w - write ' escreve no arquivo
#  r - read ' lê o arquivo
#  a - append ' adiciona ao final do arquivo
file = open('base.txt', 'w+')
file.write('Preciso estudar mais\n')
file.write('Vou estudar direto\n')
file.write('Estou estudando \n')
file.close()

# Dessa forma o cursor volta ao topo arquivo
file.seek(0, 0)
# É necessário porque read começa do finald do cursor se aberto antes
print(file.read())
print('#########')
# Lê uma linha por vez
file.seek(0, 0)
print(file.readline())
print('#########')

# Lê todas as linhas em uma lista
file.seek(0, 0)
print(file.readlines())
print('#########')

file.seek(0, 0)
for linhas in file:
    print(linhas)


#  Melhor forma de abrir arquivos

with open('base.txt', 'r') as file:
    print(file.read())

with open('base.txt', 'a+') as file:
    file.write('Última linha\n')
    file.seek(0)
    print(file.read())

# Apaga o arquivo
remove('base.txt')

base = {
    'Pessoa1': {
        'nome': 'Hugo',
        'idade': 30,
        'sexo': 'M',
    },
    'Pessoa2': {
        'nome': 'Roseane',
        'idade': 22,
        'sexo': 'F',
    },
}

d1 = json.dumps(base, indent=True)

with open('base1.json', 'w+') as file:
    file.write(d1)

with open('base1.json', 'r') as file:
    d1 = file.read()
    d1 = json.loads(d1)

for k, v in d1.items():
    print(k)
    for k1, v1 in v.items():
        print(k1, v1)

remove('base1.json')