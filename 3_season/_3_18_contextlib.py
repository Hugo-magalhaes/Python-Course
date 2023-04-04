from contextlib import contextmanager


def myopen(path_, mode_):
    try:
        arquivo = open(path_, mode_, encoding='utf8')
        yield arquivo
    except Exception as e:
        print('Ocorreu um erro', e)
    finally:
        arquivo.close()
