#Add new key-value pair
#Modify Value
#Access key
my_dict = {'name': 'Asfand', 'age':22,'city':'Islamabad'}
my_dict['profession'] = 'Developer'
my_dict['age'] = 21
# print(my_dict['city'])
# print(my_dict['age'])
# print(my_dict['profession'])
# print(my_dict)

del my_dict['profession']

for key,value in my_dict.items():
    print(key,value)

if("name","rafay") in my_dict.items():
    print("Present")
else:
    print("Not Present")


keys = ['One','Two','Three']
values = [1,2,3]

combine = dict(zip(keys,values))
# print(combine)

combine.clear()
print(combine)

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 60, 'Fourty': 40, 'Fifty': 50}

dict3 = {**dict1,**dict2}
print(dict3)

def count_char_frequencies(input_string):
  frequency_dict = {}
  for char in input_string:
    # Use get() method: if char is in dict, get its value; otherwise, default to 0
    frequency_dict[char] = frequency_dict.get(char, 0) + 1
  return frequency_dict

string1 = 'Asfand'
print(f"Frequencies for '{string1}': {count_char_frequencies(string1)}")
