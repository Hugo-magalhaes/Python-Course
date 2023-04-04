import locale
import string
from datetime import datetime
from json import dumps

origem = locale.setlocale(locale.LC_ALL, '')

valor = locale.currency(1_200_057.29, grouping=True)

data_atual = datetime(2022, 12, 4)
data_fmt = data_atual.strftime('%d/%m/%Y')

dados = dict(nome='Hugo Magalhães', valor=valor, data=data_fmt,
             cel='(11)94778-6991', origem='Wifi-Lucrativo')

# print(dumps(dados, indent=2))


msg = '''
Prezado ${nome},

Sua cobrança no valor de $valor esta prestes a vencer no dia ${data} do seu
produto ${origem}. Seu telefone ainda continua este $cel ?

Agradecemos sua atenção,

Equipe Tech Invest ltda.

'''

template = string.Template(msg)
# -- Safe garante que mesmo não havendo todas as chaves ela rodará
# print(template.safe_substitute(dados))
