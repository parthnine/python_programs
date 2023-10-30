#String Program

# Singal line string access
a = "Hello"
print(a)

# Multiple Line string access
a = """Hey !
    I am Abhijit Abdagire How can help you :)
"""
print(a)

#Strings are Arrays
a = "Hello, World!"

print(len(a))

#Slicing String
print(a[:5]) 
print(a[2:5])
print(a[2:])
print(a[-5:-2])

#String modify
print(a.upper()) #Upper Case
print(a.lower()) #Lower Case
print(a.replace("H", "J")) #Replace word

#String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

#String Format
age = 21
txt = "I am Abhi, and my age is {}"
print(txt.format(age))

