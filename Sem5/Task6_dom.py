# Дана строка (возможно, пустая), состоящая из букв A-Z:
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE, которая на выходе даст строку вида: A4B3C2XYZD4E3F3A6B28
# И сгенерирует ошибку, если на вход пришла невалидная строка. Пояснения:
# Если символ встречается 1 раз, он остается без изменений;
# Если символ повторяется более 1 раза, к нему добавляется количество повторений.
in_str = 'AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB'
def rle_func(input_string):
    import string
    alph = string.ascii_uppercase
    out_str = str()
    count = 1
    for i in range(len(input_string) - 1):
        if input_string[i] in alph:
            if input_string[i] == input_string[i+1]:
                count+=1
            else:
                out_str += input_string[i]
                if count > 1:
                    out_str += str(count)
                    count = 1
        else:
            return 'error'
    if input_string[-1] in alph:
        out_str += input_string[-1]
        if count > 1:
            out_str += str(count)
    else:
        return 'error'
    return out_str
print(rle_func(in_str))
