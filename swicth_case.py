#Switch Case

a = int(input("Enter The value of a: "))
b = int(input("Enter The value of b: "))

sign = input("Enter The Sign want to calculation(+,-,*,/,%,**): ")

match sign:
    case "+":
        result = a + b
    case "-":
        result = a - b
    case "*":
        result = a * b
    case "/" :
        result = a / b
    case "%" :
        result = a % b

    case _:
        print("Invalid sign")

print(a, sign, b, "=", result)    

#single Line Comment

"""
 This The Multi Line Comment.
"""

a = 10; b = 32; c = 30
print("The Value of the a b and c : ",a,b,c)
