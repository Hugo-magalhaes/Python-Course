def func2(a1=2, a2=3):
    return a1 * a2


def mestre(func):
    return func()


a = mestre(func2)
print(a)


def func3(a1=1, a2=2, a3=3):
    return a1 + a2 + a3


'''
Observe que os args e kwargs facilitam
passando eles a função, evita que você 
tenha limite de parâmetros para função mestre
'''


def mestre_max(funciona, *args, **kwargs):
    return funciona(*args, **kwargs)


b = mestre_max(func2, 2, 3)
c = mestre_max(func3, 1, 2, 3)
print(b, c)
