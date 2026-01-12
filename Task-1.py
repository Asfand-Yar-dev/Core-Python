# TODO
#extra func 1 parameter that passed another function
# funct 1 pass the parameter that execute another function
# function 2 and function 3 that passed through function 1 with new parameters

def function_1(x,y,func):
    return (func(x,y))
def add(x,y):
    return x + y
def multiply(x,y):
    return x * y

print(function_1(10,5,add))
print(function_1(10,5,multiply))