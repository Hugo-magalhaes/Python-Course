'''
Formatando valores

:s - Textos string()
:d - Inteiros int()
:f - Números com casas float()
:. - Quantidade de casas decimais
: (Caractere) (> ou < ou ^)(Quantidade)(Tipo - s, d ou f)

< - Valor de casas adicionadas aparecem à direita do valor inserido
> - Valor de casas adicionadas aparecem à esquerda do valor inserido
^ - Valor de casas adicionadas aparecem ao centro do valor inserido

'''


num = 150
num2 = 15000000.4
valor = 'Joao'
valor2 = 'Hugo tem {0} e deve {nome:.2f} e {nome2}'.format(
    num, nome=num2, nome2=valor)
nome = ' Rapaz foi à feira '
splitline = 'Sometimes we are given\na multiple documents\nas a single string '
print(f'{num:0>5}')
print(f'{num:0<10.2f}')
print(f'{num:0<5}')
print(f'{valor:#^10}')
print(f'{num2:,.2f}')
print(f'{num2:,}')
print(f'{num/100:.2%}')
print(f'"{nome.strip()}"')
print(f'"{nome.lstrip()}"')
print(f'"{nome.rstrip()}"')
print(splitline.splitlines())
