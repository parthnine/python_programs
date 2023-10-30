
my_dict = {
  1: "Hello", 
  (1, 2): "Hello Hi", 
  3: [1, 2, 3]
}

print(my_dict)

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

print(my_dict.get('1'))

dict3 = my_dict.copy()
print(dict3)

my_dict.pop("1")
print(my_dict)

my_dict.clear()
print(my_dict)