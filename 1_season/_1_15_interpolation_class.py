'''
s - string
d e i - int
f - float  
x e X - hexadecimal
'''
nome = 'Hugo'
preco = 10500
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
# Se colocar x hexadecimal minusculo, se X maisculo
print(' o hexadecimal de %d é %x ' % (15, 15))
print(' o hexadecimal de %d é %04x ' % (15, 15))


# Para definir uma variavel global
GLOBAL_VARIABLE = 10
