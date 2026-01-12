def func1(x, y):
    return x + y

def func2(a, b):
    result = func1(a, b)
    return result * 2

def func3(p, q):
    result = func2(p, q)
    return result - 5

print(func3(2, 3))
