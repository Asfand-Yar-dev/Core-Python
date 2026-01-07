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
    