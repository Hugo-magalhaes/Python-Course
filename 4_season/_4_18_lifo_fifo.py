# FIFO e LIFO
# Fila e pilha


# First in first out (stack - Pilha)
# Last in first out (queue - Fila)


# ! Importante para grande volume de dados
#  - Tipo de FIFO (Pilha) melhor que a lista normal
from collections import deque

fila: deque[int] = deque()
fila.append(3)
fila.appendleft(2)
fila.pop()
fila.popleft()
