class NameError(Exception):
    ...


class Name2Error(Exception):
    ...
    # Linguagens de programação utilizam throw e raise
    # Python é raise


def levantar():
    exc = NameError('A mensagem do meu erro', 'erro 2 ', 'chamada incorreta')
    exc.add_note('Um erro aqui')
    raise exc


try:
    levantar()
except (NameError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    exc = Name2Error('Vou lançar um segundo erro')
    exc.__notes__ += error.__notes__.copy()
    raise exc
