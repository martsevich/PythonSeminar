# with open('example0_2.txt', 'r', encoding='utf-8') as file:
#     file_text = file.read().replace('\n', ' ')
# list_text = file_text.split(' ')
# print(list_text)
# len_text = list(map(len, list_text))
# max_words = list(filter(lambda x: len(x) == max (len_text), list_text))
# print(max_words)

def read_last(lines, file):
    with open(file, 'r', encoding='utf-8') as file:
        file_text = file.read().split('\n')
        print(file_text)
    for i in range(len(file_text)-lines, len(file_text)):
        print(file_text[i])

read_last(2, 'example0_2.txt')



