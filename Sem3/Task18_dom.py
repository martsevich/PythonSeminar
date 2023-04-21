# Требуется найти в списке A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в списке.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# # *Пример:*
# # 5
#     1 2 3 4 5
#     6
#     -> 5
import random

#listn = [8, 3, 1, 5, 7, 10]
listn = []
N = int(input('Ввод количества элементов: '))
for i in range(0, N):
    listn.append(random.randint(0, N))
print(listn)
X = int(input('Ввод числа для поиска: '))
count = 0
a = 1
for i in range(len(listn)):
    for j in range(len(listn)):
        if X - a == listn[j]:
            count = listn[j]
            break
    else:
        a += 1
print(f'Близкий по величине элемент: {count}')

