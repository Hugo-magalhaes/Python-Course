# Variaveis mutaiveis : Lists, Dicionarios
# Imutaveis : Tuplas, Strings, True, False, None, numero

def lista(lista_nova, lista_1=[]):
    lista_1.extend(lista_nova)
    return lista_1


lista2 = lista([1, 2, 3, 4])
lista3 = lista([6, 7])

# Observe que ambos são iguais devido lista_1 ser mutavel
print(lista2)
print(lista3)


def lista_funcional(lista_nova, lista_1=None):
    if lista_1 is None:
        lista_1 = []
    lista_1.extend(lista_nova)
    return lista_1


lista4 = lista_funcional([1, 2, 3, 4])
lista5 = lista_funcional([6, 7])

print(lista4)
print(lista5)
