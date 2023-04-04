nome = input('Qual seu nome? \n')
idade = int(input('Qual sua idade? \n'))
peso = int(input('Qual seu peso? \n'))
altura = float(input('Qual sua altura? \n'))
imc = peso/(altura**2)
ano_atual = int(input('De que ano está falando? \n'))
fez_aniversário = int(input('Já fez aniversário [1] para sim e [0] para não? \n'))

if not fez_aniversário:
    ano_nascimento = ano_atual - idade - 1
else:
    ano_nascimento = ano_atual - idade

# print vazio pula linha em branco
print()
print(f' {nome} tem {idade} anos, {altura} e pesa {peso}Kg \n O IMC de {nome } é {imc:.2f} '
      f'\n {nome} nasceu em {ano_nascimento}')
