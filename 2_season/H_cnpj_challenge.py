import H_fuctions as hf

# cnpj_orig = input('Digite o cnpj: ')
# cnpj_orig = '04.252.011/0001-10'
# cnpj_orig = '40.688.134/0001-61'
# cnpj_orig = '71.506.168/0001-11'
# cnpj_orig = '12.544.992/0001-05'

# novo_cnpj = hf.conta(cnpj_orig)
# print(novo_cnpj)

cnpj = hf.gerador_cnpj()

print(cnpj)

hf.pontos(cnpj)