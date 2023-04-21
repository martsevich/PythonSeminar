# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
import random

listn = list()
for i in range(0, 10):
    listn.append(random.randint(0, 10))
k = int(input('Vvod K: '))
print(listn)
listn = listn[k:] + listn[:k]
print(listn)