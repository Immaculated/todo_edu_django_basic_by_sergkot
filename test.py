
list_ = [1, 2, 3, 4, 5]


def func():
    for i in range(10):
        return i


def func_generator():
    for i in range(10):
        yield i


print(func())
print(func_generator())
# print(next(gen))
# print(next(gen))
# print(next(gen))