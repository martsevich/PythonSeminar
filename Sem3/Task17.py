# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

listn = list()
count = 0
while True:
    n = int(input('vvod: '))
    listn.append(n)
    if listn.count(n) == 1:
        count += 1
    print(count)
    print(listn)