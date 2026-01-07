print("Hello World")

print("2+2")

print(2+2)

name="Asfand Yar"
print("My name is", name)

name=input("Enter your name:")
print("Hello", name)


if 5>2:
    print("Five is greater than everyone")


x,y,z=10,20,30
print(x)
print(y)
print(z)
print(type(z))

def myfunct():
    global x
    x="Hello Charlie"
myfunct()

print(x)

def add(num1,num2):
    return num1+num2

result=add(5,10)
print(result)
    
number=int(input("Enter your age:"))
if number<18:
    print("You are a minor")
elif number==18:
    print("Your are a young adult")
elif number>18:
    print("Your are an adult")
else:
    print("Invalid Input")
    

x=3+5j
y=5j
z=-5j

print(type(x), type(y), type(z))

import random
print(random.randrange(1,10))

for i in range(5):
    print(i)

names=["Asfand", "Ali", "Ahmed", "Adeel"]
numbers=[1,2,3,4,5,6,7,8,9]
print(names)
numbers.append(10)
print(numbers[5])