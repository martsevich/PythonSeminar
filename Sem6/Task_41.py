# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.

use_list = int(input("Eneter: "))
list_use = [int(input(f"{i+1} number = ")) for i in range(use_list)]
print(*list_use)
count = 0
for i in range(1, len(list_use)-1):
    if list_use[i-1] < list_use[i] > list_use[i+1]:
        count+=1
print(count)