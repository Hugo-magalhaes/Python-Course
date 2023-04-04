lista = ['maria', 'joão', 'a', 'coisas', 'aleatorias', 'aro']

# Dessa forma ele pega o intervalo que ele se encontra nas variáveis
n1, n2, *_, nf = lista
# print(_) # Defini uma lista que não será utilizado

x = 10
y = 'hugo'

x, y = y, x

# Operador ternário
idade = input('Qual sua idade? ')

analise = idade if idade.isnumeric() else input('Coloque a sua idade: ')
idade = int(analise)
e_de_maior = (idade >= 18)
msg = 'Pode acessar' if e_de_maior else 'Não pode acessar'
print(msg)

# Operador or
nome = input('Qual seu nome? ')
print(nome or 'Você não digitou nada')
