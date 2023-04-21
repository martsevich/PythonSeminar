# Вводятся числа пока не введут 0. Найти сумму четных чисел.

#summa = 0
#while True:
#    a = int(input())
#    if a == 0:
#        break
#    if a % 2 == 0:
#        summa += a
#print(summa)

b = [1, 2, 5, 6, -8]
ind = 0
while ind < len(b):
   if b[ind] < 0:
       print(f'Yes {b[ind]}')
       break
   ind += 1
   print(ind)
else:
   print('No')

# # Значение переменной-итератера используется:
# for i in range(1, 11):
#     print(i**2)
#
# # Значение переменной-итератера неиспользуется:
# for i in range(5):
#     print('HELLO')
#
# some_list = [-3, 4, 5, 8, 1]
# for a in some_list:
#     print(a)
#
# for ind in range(0, len(some_list)): # 0, 1, 2, 3, 4
#     print(some_list[ind])
#
# for i in [1, 2, 3, -4, 5]:
#     if i < 0:
#         print('Yes')
#         break
# else:
#     print('No')
#
# a = []
# a.append(10)
# print(a)
#
# a = []
# print(a)
# a[1] = 200
# a[2] = 300
# print(a)
#
# # Вводится два числа а и b. Найти все простые числа в диапозоне от а до b.
# a = int(input())
# b = int(input())
# for i in range(a, b + 1):
#     for j in range(2, i // 2 + 1):
#         if i % j == 0:
#             break
#     else:
#         print(i)