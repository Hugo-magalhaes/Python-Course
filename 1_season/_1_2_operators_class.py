nome = input('Qual seu nome? ')
if 'u' in nome:
    qtd = int(input('Quantos letras tem seu nome? '))
    if qtd > 5:
        print('Seu nome é grande tem', qtd, 'letras')
    else:
        print('Seu nome é pequeno tem', qtd, 'letras')

else:
    print('Você não tem u no nome')

# é possível utilizar '...' e pass para manter uma posição sem ter código

val = True

if val:
    pass
else:
    print('Tchau')
