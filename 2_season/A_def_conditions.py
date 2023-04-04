def saudacao(apresentacao='Olá', nome=''):
    print(f'{apresentacao}, meu nome é {nome}')


saudacao('Oi', 'Hugo')


def soma(n1, n2, n3):
    print(n1 + n2 + n3)


soma(1, 2, 3)


def acrescimo(num, percentual):
    print(num + num*percentual/100)


acrescimo(2092, 5.67)


def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        print('Fizz Buzz')
    elif num % 5 == 0:
        print('Buzz')
    elif num % 3 == 0:
        print('Fizz')
    else:
        print(num)


fizzbuzz(9)