import pandas as pd

data = {'nome': ['hugo', 'miguel', 'joão'],
        'idade': [17, 22, 19],
        'cidade': ['São Paulo', 'Recife', 'Santa Catarina']}
data1 = [['hugo', 17, 'São Paulo'],
         ['Miguel', 22, 'Recife'],
         ['João', 19, 'Santa Catarina']]

dados = pd.DataFrame(data)
dados1 = pd.DataFrame(data1, columns=['nome', 'age', 'cidade'])

#  Pode ser criar codições de mascáras
mask = dados1.loc[:, 'age'] > 17
dados1[mask]  # Mesma idea do que está no print
# print(dados1[dados1['age'] > 17])
dados1['Idade em meses'] = dados1['age']*12

# Python operators | or & and ~ not
data2 = {
    'even': range(20, 0, -2),
    'odd': range(1, 21, 2)
}
df = pd.DataFrame(data2)
# print(df.apply(sum)) # soma as colunas
# print(df.apply(sum, axis=1)) # soma as linhas


def rest_lis(row):
    ret_val = [False, False]
    if row['even'] > 6:
        ret_val[0] = True
    if row['odd'] > 6:
        ret_val[1] = True
    return ret_val


print(df.apply(rest_lis, axis=1, result_type='expand'))

#! Ndarray é diferente de pandas só suporta um array com um formato de dados
#! Mas ele suporta listas de diversas dimensões
