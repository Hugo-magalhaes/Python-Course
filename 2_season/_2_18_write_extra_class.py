import os

#  / == \\ if it doesn't work use r in the begining

# r - read, w - write, x - creation
# t - text mode,a - append mode, b - binary
# r+/w+ - read and write

#  The difference between a and w is w clean the whole file

with open('teste.txt', 'w+', encoding='utf-8') as arquivo:
    arquivo.writelines(
        ('Um \n', 'Dois \n', 'Três \n')
    )
    arquivo.seek(0, 0)
    print(arquivo.read())
    arquivo.seek(0, 0)
    print(arquivo.readline(), end='')
    print(arquivo.readline().strip())
    for linha in arquivo.readlines():
        print(linha.strip())

# os.unlink(arquivo) == os.remove(arquivo)
# os.rename() pode alterar o caminho do arquivo
