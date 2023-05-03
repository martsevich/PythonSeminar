# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea shore shells
# Output: 13

# text = input() + " "
# count = 0
# unical = set()
# for i in range(len(text)):
#     if text[i] == " ":
#         if " " not in (text[count: i]):
#             unical.add(text[count:i])
#             count = i + 1
# print(len(unical))

# some_str = input().split()
# print(len(set(some_str)))

# решение препода:
some_str = input()
some_set = set()
temp_word = ''
for letter in some_str:
    if letter != ' ':
        temp_word += letter
    else:
        if temp_word:
            some_set.add(temp_word)
        temp_word = ''
some_set.add(temp_word)
print(len(some_set))
