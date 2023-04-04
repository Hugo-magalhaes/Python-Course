while True:
    entrar = input(' Deseja utilizar a calculadora, [s]im ou [n]ão? ')
    if entrar == 'n':
        print('Saindo...')
        break  # Pausa o laço aqui

    num1 = input('Digite o primeiro número:')
    operador = input('Qual operação deseja realizar +, -, / ou * ? ')
    num2 = input('Digite o primeiro número:')

    if not num1.isnumeric() or not num2.isnumeric():
        print('Preciso que insira números!!!')
        continue  # Reinicia o laço sem erro

    if operador == '+':
        print(float(num1)+float(num2))
    elif operador == '-':
        print(float(num1)-float(num2))
    elif operador == '/':
        print(float(num1)/float(num2))
    elif operador == '*':
        print(float(num1)*float(num2))
    else:
        print('Precisa-se de um operador válido')
        continue
