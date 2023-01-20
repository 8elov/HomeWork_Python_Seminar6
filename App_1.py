# 1. Создайте список из случайных чисел. Найдите количество различных элементов в нем.

import random

n = int(input('Сколько элементов в списке? '))
list = []

for i in range(n):
    list.append(random.randint(1, 10))
print('Дан список:', list)

count_diff = len(set(list))
print('Количество различных элементов:', count_diff)