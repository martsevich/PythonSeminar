# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B
# с помощью рекурсии.
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

A = int(input("A "))
B = int(input("B "))
def AB (A, B):
    if B == 0:
        return 1
    return A * AB(A, B-1)
print(AB(A, B))

# A = int(input("A "))
# B = int(input("B "))
# A1 = 1
# i = 0
# if B < 0:
#     print("Error")
# else:
#     while i < B:
#         C = A1 * A
#         A1 = C
#         i += 1
# print(A1)