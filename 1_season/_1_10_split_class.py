
string = 'O Brasil é o país do futebol, Brasil é o penta. E o Cátar é só um país esquecido'
# Essa função separa uma string a partir de um separador escolhido
l1 = string.split(' ')
l2 = string.split(',')

contagem = 0
palavra = ''
# O valor nesse caso conta a quantiade de vezes que uma mesma palavra aparece
for valor in l1:
    qtd_vezes = l1.count(valor)
    # print(f' A palavra {valor} apareceu {qtd_vezes} vezes')

    if qtd_vezes > contagem:
        palavra = valor
        contagem = qtd_vezes

print(f'A palavra que mais apareceu é {palavra} {contagem}x')

# Dessa forma a segunda frase vai perder o espaço inicial e Ter capital letter
for valor in l2:
    print(valor.strip().capitalize())
    qtd_vezes = l2.count(valor)

    if qtd_vezes > contagem:
        palavra = valor

print(f'A palavra que mais apareceu é {palavra} {qtd_vezes}x')

# Junta valores de uma lista com um espaço (valor escolhido)
string1 = ' '.join(l1)
string2 = 'Sei de nada'

# A função enumerate cria tuplas com indice e o valor
for indice, valor in enumerate(string2):
    print(indice, valor)

for indic in enumerate(string2):
    indic2, valor = indic
    print(indic2, valor)

# Forma de encontrar o valor da lista dentro dae outra lista
lista = [[1, 23, 34], [4, 56, 7], [3, 4, 5]]
print(lista[1][1])
