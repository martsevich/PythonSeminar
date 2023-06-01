# Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая планета ровно одна

from functools import reduce
def find_farthest_orbit(list_of_orbits):
    # list_of_orbits = list(filter(lambda x: x[0] != x[1], list_of_orbits))
    # print(*list_of_orbits)
    # list_of_orbits = reduce(lambda a, b: a if a[0] * a[1] > b[0] * b[1] else b, list_of_orbits)
    # print(*list_of_orbits)
    return max(list_of_orbits, key=lambda x: (x[0] != x[1])*x[0]*x[1]) #x[0]!=x[1])-булевая переменная (true or false: 0 or 1)

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))

list = [1,2,3,4,5]
t = sorted(list, key=lambda x: x%2==0)
print(t)