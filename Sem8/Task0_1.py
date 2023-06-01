#пользователь вводит количество строк. затем сами строки. Нужно записать в ноый текстовый файл все эти строки.
#далее пользователь вводит символ, нужно найти количество этого символа в новом файле.

num_string = int(input('Введите количество строк: '))
string_list = []
print('Введите строку: ')
for string in range (num_string):
    string_list.append(input(f'{string}:')+'\n')
with open('example0_1.txt', 'w', encoding='utf-8') as file:
    file.writelines(string_list)
user_sing = input('Введите символ для поиска: ')
with open('example0_1.txt', 'r', encoding='utf-8') as file:
    find_sign = file.read()
count = 0
for i in find_sign:
    if user_sing == i:
        count += 1
print(f'Количество символов {count}')
