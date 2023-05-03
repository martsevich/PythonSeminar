# Дана строка (возможно, пустая), состоящая из букв A-Z:
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE, которая на выходе даст строку вида: A4B3C2XYZD4E3F3A6B28
# И сгенерирует ошибку, если на вход пришла невалидная строка. Пояснения:
# Если символ встречается 1 раз, он остается без изменений;
# Если символ повторяется более 1 раза, к нему добавляется количество повторений.

some_list = {1: 'A,B,C,D,E,F,G'}
N = input('Введите: ')
s = 0
i = 0
for i in N:
    for key, val in some_list.items():
        if i in val:
            if val == val:
                s = s + key
print(f'A{s}')