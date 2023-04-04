from datetime import datetime

from dateutil.relativedelta import relativedelta

emprestimo = 1_000_000
fmt = '%d/%m/%Y'
data = '20/12/2020'

data_pmt = datetime.strptime(data, fmt)
delta = relativedelta(years=5)
data_fim = data_pmt + delta

delta_total = data_fim - data_pmt
meses = int(delta_total.days/30)

valor = 0.00
valor_emprestimo = emprestimo/meses
data_parcela = data_pmt

while data_parcela < data_fim:
    valor += valor_emprestimo
    data_parcela += relativedelta(months=+1)
    print(f'{data_parcela.strftime(fmt)}   R$ {valor:,.2f}')
