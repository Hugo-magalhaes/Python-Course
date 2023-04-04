from typing import TypeVar

T = TypeVar('T')


def get_item(list: list[T], index: int) -> T:
    return list[index]


lista_int = get_item([1, 2, 3], 1)
lista_str = get_item(['1', '2', '3'], 1)

print(lista_int)
print(lista_str)
