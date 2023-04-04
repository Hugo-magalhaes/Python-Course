string = '0123456789012345678901234567890123456789012345678901234567890123456789'

quebra_string = [
    string[indice:indice + 10]
    for indice in range(0, len(string), 10)
]
print(quebra_string)

nova_string = '.'.join(quebra_string)

print(nova_string)
