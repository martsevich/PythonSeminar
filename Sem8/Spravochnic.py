# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

def input_data():
    lastname = input('Введите фамилию: ')
    forename = input('Введите имя: ')
    patroname = input('Введите отчество: ')
    N_fone = input('Введите номер телефона: ')
    with open('spravochnic.txt', 'a', encoding='utf-8') as file:
        file.write(lastname + '\n')
        file.write(forename + '\n')
        file.write(patroname + '\n')
        file.write(N_fone + '\n')
        file.write(' ' + '\n')
def data_one():
    add = input('Для поиска введите 1, для добавления - 2: ')
    if add == '1':
        search_data()
    elif add == '2':
        input_data()
    else:
        print('Введено неверное значение!')
def search_data():
    search = input('для поиска по фамилии введите 1, по имени - 2: ')
    result = list()
    if search == '1':
        with open('spravochnic.txt', 'r', encoding='utf-8') as file:
            text = list(file.read().split())
        lastname_search = input('Введите фамилию: ')
        for i in range(len(text)):
            if text[i] == lastname_search:
                result.append(text[i])
                result.append(text[i+1])
                result.append(text[i+2])
                result.append(text[i+3])
        if lastname_search not in text:
            print('Фамилия не найдена!')

    if search == '2':
        with open('spravochnic.txt', 'r', encoding='utf-8') as file:
            text = list(file.read().split())
        forename = input('Введите имя: ')
        for i in range(len(text)):
            if text[i] == forename:
                result.append(text[i - 1])
                result.append(text[i])
                result.append(text[i + 1])
                result.append(text[i + 2])
        if forename not in text:
            print('Имя не найдено!')

    else:
        print('Введено неверное значение!')
    return print(' '.join(result))

def output_data():
    with open('spravochnic.txt', 'r', encoding='utf-8') as file:
        text = file.read()
        print(text)

data_one()
# input_data()




