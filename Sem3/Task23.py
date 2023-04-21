# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
import random

listn = list()
for i in range(0, 10):
    listn.append(random.randint(-10, 10))
print(listn)
listt = list()
count = 0
for i in range(len(listn)-1):
    if listn[1] < listn[i + 1]:
        count += 1
        listt.append(f'{listn[1]} < {listn[i + 1]}')
print(f'{count} {listt}')

