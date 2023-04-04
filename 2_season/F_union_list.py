from itertools import zip_longest

l_1 = [1, 2, 3, 4, 5, 6, 7, 8]
l_2 = [1, 2, 3, 4, 5]

soma = [x+y for x, y in zip(l_1, l_2)]

print(soma)

l_soma = []
for i in range(len(l_2)):
    l_soma.append(l_1[i]+l_2[i])

l_sum = []
for i, _ in enumerate(l_2):
    l_sum.append(l_1[i]+l_2[i])

sum_l = [x+y for x, y in zip_longest(l_1, l_2, fillvalue=0)]

print(sum_l)