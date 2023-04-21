some_str = 'hello'

#for letter in some_str:
#    print(letter)

#for ind in range(0, len(some_str)):
#    print(some_str[ind])

#print(some_str[-2])

#print(some_str[::-1])

#print(*range(0, 10))

#some_list = []
#for _ in range(10):
#    number = int(input())
#    some_list.append(number)
#print(some_list)

#some_list = [int(input()) for _ in range(10)]
#print(some_list)

#import random
#some_list = []
#for _ in range(10):
#    number = random.randint(1, 10)
#    some_list.append(number)
#print(some_list)

#print(some_list.count(6))

#print(7 in some_list)

# a = [1, 2, 3]
# b = tuple(a)
# for i in b:
#    print(i)
# print(b[0])

#a = 1, 2
#print(type(a))

# a = set()
# for i in range(1, 10):
#     a.add(i)
# print(a)

# import random
# import time
#
# some_list = [random.randint(1, 10000) for i in range (10**6)]
# some_set = set(some_list)
#
# start = time.perf_counter()
# print(9999 in some_list)
# end = time.perf_counter()
# duration1 = end - start
#
# start = time.perf_counter()
# print(9999 in some_set)
# end = time.perf_counter()
# duration2 = end - start
#
# print(duration1/duration2)

# some_dict = {1: '1', 2: '2', 3: '3'}
# print(some_dict.get(2))
# some_dict['4'] = '4'
# print(some_dict)

#неизменяемый:
# str
# int
# float
# bool
# tuple
# frozenset

#изменяемый:
# list
# dict
# set

a = [1, 2, 3]
b = ['1', '2', '3']
c = {}
for ind in range(0, len(a)):
    c[a[ind]] = b[ind]
print(c)

