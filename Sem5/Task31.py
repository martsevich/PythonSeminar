# Последовательностью Фибоначчи называется последовательность чисел
# a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1). Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21

def fib(n):
    if n in (0, 1):
        return n
    return fib(n-1) + fib(n-2)
print(fib(7))

def fib_while(n):
    first = 0
    second = 1
    temp_number = first + second
    count = 2
    while count < n:
        first, second = second, temp_number
        temp_number = first + second
        count += 1
    print(temp_number)
fib_while(7)
