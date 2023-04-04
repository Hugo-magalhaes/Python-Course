string = 'Qualquer coisa'

contador = 1

while contador <= len(string):
    letra = string[contador]
    print(letra)
    contador += 1

else:
    # O break não leva ao else
    print('O laço finalizou com êxito')
