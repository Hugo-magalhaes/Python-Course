lista = [
    [2, 10, 8, 1, 6, 3, 5, 7, 4, 9],
    [10, 6, 1, 1, 3, 7, 2, 1, 1, 7],
    [4, 8, 3, 6, 9, 5, 4, 4, 3, 10],
    [4, 1, 4, 4, 7, 5, 5, 10, 5, 8],
    [5, 3, 9, 3, 9, 9, 2, 1, 6, 3],
    [6, 3, 2, 1, 3, 6, 10, 5, 10, 4],
    [6, 1, 4, 5, 7, 9, 3, 2, 10, 8],
    [4, 3, 6, 1, 4, 3, 5, 5, 10, 9],
    [8, 5, 1, 2, 1, 10, 5, 10, 3, 2],
    [1, 4, 10, 5, 2, 9, 3, 7, 8, 6]
]

n = 0
lista_nodup = []
for m_list in lista:
    for v in m_list:
        if v not in lista_nodup:
            n += 1
            lista_nodup.append(v)
            # print(lista_nodup)

        else:
            print(v)
            n = 0
            lista_nodup = []
            print()
            break

        if n > 9:
            n = 0
            if len(lista_nodup) == 10:
                print(-1)

            lista_nodup = []
            print()
            break


def find_first_dup(param_list):
    check_numbers = set()
    first_dup = -1

    for number in param_list:
        if number in check_numbers:
            first_dup = number
            break

        check_numbers.add(number)

    return first_dup


for me_list in lista:
    print(find_first_dup(me_list))

