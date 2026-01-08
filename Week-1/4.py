# m= 'This string\nspans multiple\nlines.'
# print(m)

# m="I am learning Javascript"
# print(m.replace("Javascript", "Python"))

# name=(input("Enter Your Name:"))
# print(name.lower())
# print(name[0])
# print(len(name))

User={
    "Name": "Asfand Yar",
    "Age": 22,
    "Education": "BS Computer Science",
    "Email": "asfandyar273263@gmail.com"
}

User["Age"]=21
User["Height"]="5.7"

for key in User:
    print(type(key), "=>" ,User[key])
    print(len(User))
