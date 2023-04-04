
def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total


soma(1, 23, 4, 5, 6)
