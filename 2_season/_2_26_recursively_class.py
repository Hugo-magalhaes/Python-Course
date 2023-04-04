def recursiva(inicio=0, final=10):
    print(inicio, final)
    if inicio >= final:
        return final
    inicio += 1
    return recursiva(inicio, final)

# Há um limite de recursividade
# sys.setrecursionlimit()
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)


print(factorial(20))
