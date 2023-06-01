# with open('example.txt', 'r', encoding='utf-8') as file:
#     # file.seek(0)          #считывание по байтам
#     text = file.read()
#     print(text)
#
# with open('example.txt', 'r', encoding='utf-8') as file:
#     while True:
#         line = file.readline()
#         if not line:
#             break
#         print(line[:-1]) # [:-1] - убирает отступы м/д строками

# with open('example.txt', 'r', encoding='utf-8') as file:
#     text = file.read()
#     print(text.splitlines())
#
# with open('example.txt', 'r', encoding='utf-8') as file:
#     text = file.readlines()
#     print(text)

# with open('example.txt', 'w', encoding='utf-8') as file:    # w - запись в  файл наверх, перезапись
#     some_list = ['hello', 'world', 'how', 'are', 'you']
#     for el in some_list:
#         file.write(el + '\n')

# import json
# some_dict = {1:2, 2:3}
# with open('example.json', 'w', encoding='utf-8') as file:
#     json.dump(some_dict, file)

with open('example.txt', 'w', encoding='utf-8') as file:
    some_dict = {1: 2, 2: 3}
    file.write(str(some_dict)[1:-1])