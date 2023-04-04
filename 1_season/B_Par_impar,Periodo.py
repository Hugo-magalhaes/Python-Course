import time

num = input('Digite um número: ')

if not num.isdigit():
    print('Valor não numérico informado')
elif int(num) % 2 == 0:
    print('Seu número {} é par'.format(num))
else:
    print('Seu número {} é ímpar'.format(num))

hora = input('Que horas são? \n')

if time.strptime(hora, '%H:%M') <= time.strptime('11:00', '%H:%M'):
    print('Bom dia são {}'.format(hora))
elif time.strptime(hora, '%H:%M') <= time.strptime('17:00', '%H:%M'):
    print('Boa tarde são {}'.format(hora))
else:
    print('Boa noite são {}'.format(hora))

nome = input('Digite seu nome: ')

if len(nome) <= 4:
    print('Nome mixuruca.')
elif len(nome) <= 6:
    print('Isso é um nome, pelo menos.')
else:
    print('Que nomão em.')

hora = input('Que horas são? \n')

if int(hora[:2]) <= 11:
    print('Bom dia são {}'.format(hora))
elif int(hora[:2]) <= 17:
    print('Boa tarde são {}'.format(hora))
else:
    print('Boa noite são {}'.format(hora))
