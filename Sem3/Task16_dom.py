# Требуется вычислить, сколько раз встречается некоторое число X в списке A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# # *Пример:*
# # 5
#     1 2 3 4 5
#     3
#     -> 1
# import random
#
# listn = []
# N = int(input('Ввод количества элементов: '))
# for i in range(0, N):
#     listn.append(random.randint(0, N))
# print(listn)
# X = int(input('Ввод числа для поиска: '))
# count = 0
# for i in range(len(listn)):
#     if X == listn[i]:
#         count = count + 1
# print(f'Количество чисел в списке: {count}')

#препода:
a = [int(input()) for _ in range(int(input()))]
x = int(input('введите искомое число: '))
print(a.count(x))