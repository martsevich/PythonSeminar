#В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для
#них новыми партами. За каждой партой может сидеть два учащихся. Известно количество учащихся в
#каждом из трех классов. Выведите наименьшее число парт, которое нужно приобрести для них.
#Input: 20 21 22(ввод чисел НЕ в одну строку)
#Output: 32
n1 = int(input('Input n1'))
n2 = int(input('Input n2'))
n3 = int(input('Input n3'))
st = n1 + n2 + n3
d = (st // 2 + st % 2)
print(d)