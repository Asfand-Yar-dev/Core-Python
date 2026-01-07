#Age Checker
age=int(input("Enter your age:"))
if age>=18:
    print("Adult")
elif age<18:
    print("Minor")
elif age>=120:
    print("Invalid Age")

#Number Sum
def sum_number(n):
    total=0
    for i in range(n):
        number=(int(input(f"Enter a number {i+1}:")))
        total+=number
    print(f"Total sum: {total}")

n=int(input("How many numbers do you want to sum?"))
sum_number(n)

#List Manager
names = []
for i in range(5):
    name = input(f"Enter name {i+1}: ")
    names.append(name)
print("\n📋 All names:")
for name in names:
    print(f"- {name}")
search_name = input("\nSearch name: ")
if search_name in names:
    print("✅ Found!")
else:
    print("❌ Not Found!")

#Multiplication Table
def mul_table(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
number=int(input("Enter a number to see its multiplication table:"))
mul_table(number)

#Simple Calculator
def calculator():
    num1=float(input("Enter first number:"))
    operator=input("Enter operator (+, -, *, /):")
    num2=float(input("Enter second number:"))
    
    if operator=='+':
        print(f"Result: {num1 + num2}")
    elif operator=='-':
        print(f"Result: {num1 - num2}")
    elif operator=='*':
        print(f"Result: {num1 * num2}")
    elif operator=='/':
        if num2!=0:
            print(f"Result: {num1 / num2}")
        else:
            print("Error: Division by zero")
    else:
        print("Invalid operator")
calculator()

#Even-Odd Checker
number=int(input("Enter a number:"))
if number%2==0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")