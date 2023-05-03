import random
some_str = ''.join([chr(random.randint(32, 100)) for _ in range(10)])

# import time
# start = time.perf_counter()
# for letter in set(some_str):
#     a = letter, some_str.count(letter)
# end = time.perf_counter()
# duration1 = end - start
#
# start = time.perf_counter()
# for letter in set(some_str):
#     amount = 0
#     for letter1 in some_str:
#         if letter == letter1:
#             amount += 1
#     a = letter, amount
# end = time.perf_counter()
# duration2 = end - start
# print(duration2 / duration1)

print(some_str)
count_dict = {} # a: 1
for letter in some_str:
    if letter not in count_dict:
        count_dict[letter] = 1
    else:
        count_dict[letter] = count_dict[letter] + 1
print(count_dict)
