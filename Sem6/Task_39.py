# Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество элементов во втором массиве. Затем элементы второго массива

use_list1 = int(input("Enter 1: "))
list_one = [int(input(f"{i+1} number = ")) for i in range(use_list1)]
use_list2 = int(input("Enter 2: "))
list_two = [int(input(f"{i+1} number = ")) for i in range(use_list2)]
print(*list_one)
list_two = set(list_two)
print(*list_two)
temp_list = [i for i in list_one if not i in list_two]
print(*temp_list)