#1. Сумма трех Посчитайте сумму трех введенных целых чисел
n1 = int(input('Введите число 1:'))
n2 = int(input('Введите число 2:'))
n3 = int(input('Введите число 3:'))
print(f'Summa: {n1 + n2 + n3}')

#2. Площадь Пользователь вводит стороны прямоугольника, выведите его площадь
n1 = int(input('Введите сторону 1:'))
n2 = int(input('Введите сторону 2:'))
print(f'P = {n1 * n2}')

#3. 1. Одинаковая четность Даны два целых числа: A, B. Проверить истинность высказывания: "Числа A и B имеют одинаковую четность".
n1 = int(input('Введите число А: '))
n2 = int(input('Введите число В: '))
if (n1 % 2 == 0 and n2 % 2 == 0) or (n1 % 2 != 0 and n2 % 2 != 0):
    print(True)
else:
    print(False)

#4. Одно положительное Даны три целых числа: A, B, C. Проверить истинность высказывания: "Хотя бы одно из чисел A, B, C положительное".
n1 = int(input('Введите число А: '))
n2 = int(input('Введите число B: '))
n3 = int(input('Введите число C: '))
if n1 > 0 or n2 > 0 or n3 > 0:
    print (True)
else:
    print (False)

#5. Меньшее из двух Пользователь вводит два целых числа. Выведите меньшее из них.
n1 = int(input('Введите число 1: '))
n2 = int(input('Введите число 2: '))
if n1 > n2:
    print(n2)
elif n1 == n2:
    print('n1 = n2')
else:
    print(n1)

#6.Четырехзначное? Пользователь вводит целое число. Выведите YES, если это число является четырехзначным, и NO в противном случае.
a = int(input('Input num'))
if len(a) == 4:
    print('Yes')
else:
    print('No')

#За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров?
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
#Input:
#n = 700
#m = 750
#Output:
#2
n = int(input('Input n'))
m = int(input('Input m'))
print(n * 31 / m)