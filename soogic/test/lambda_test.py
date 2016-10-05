from time import clock

g = lambda x, y: x - y
print g(1000, 432)


def multiply(x):
    return lambda y: x * y


formula_1 = multiply(2)
formula_2 = multiply(3)

print formula_1(111)
print formula_2(749)
print multiply(7)(11)

foo = [0, 1, 3, 5, 6, 7, 9, 11, 13, 15, 17, 18, 20, 21]


start = clock()
print filter(lambda x: x % 3 == 0, foo)
print map(lambda x: x % 3 == 0, foo)
print reduce(lambda x, y: x - y, foo)

print filter(lambda x: x * 3 + 7, foo)
print map(lambda x: x * 3 + 7, foo)
finish = clock()
print finish - start
