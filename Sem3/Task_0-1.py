import random

listn = list()
for i in range(0, 10):
    listn.append(random.randint(-10, 10))
print(listn)
for i in range(len(listn)-1, 0, -1):
    listn.append(random.randint(-10, 10))
    if listn[i] > listn[i - 1] and listn[i] > listn[i + 1]:
        print(i, '=', listn[i])
        break

