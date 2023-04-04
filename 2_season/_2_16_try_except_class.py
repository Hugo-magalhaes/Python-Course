def conversor(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass


numero = conversor(input('Digite um número:'))

if numero is not None:
    print(numero * 2)
else:
    print('Log: erro')

try:
    print(8/0)
except ZeroDivisionError:
    print('erro')
else:
    print('Não houve erros')
# Sempre é executado e fecha o arquivo
finally:
    print('fecha arquivo')
