# def test(x):
#     return lambda n: n % x == 0
# func = test(2)
# print(func(8))
#
# #замыкание
# def test(x):
#     def f(n):
#         return n % x == 0
#     return f
#
# func = test(2)
# print(func(8))

some_list = [1,2,3,4]
other_list = ['a', 'b', 'c', 'd']
d = dict(zip(other_list, some_list))
def func(a,b,c,d):
    return a+b+c+d
print(func(**d))

def func2(**kwargs):
    print(kwargs)
func2(a=4,b=7,c=2)

def func3(*args):
    return sum(args)
print(func3(1,2,3,4,5))

from collections import defaultdict
d = defaultdict(int)
d['a'] += 1
print(d)