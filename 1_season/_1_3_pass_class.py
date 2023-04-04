# é possível utilizar '...' e pass para manter uma posição sem ter código

val = True

if val:
    pass
else:
    print('Tchau')

if not val:
    ...
else:
    print('Foda')
