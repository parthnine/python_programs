import numpy as np;

a = np.array([5, 6, 8, 100])
b = np.array([2, 5, 10, 30])

print("Addtion is : ")
addAns = np.add(a, b)
print(addAns)
 
print("Subtraction is : ") 
subAns = np.subtract(a, b)
print(subAns)

print("Multiplication is : ")
mulAns = np.multiply(a, b)
print(mulAns)
 
print("Division is : ")
divAns = np.divide(a, b)
print(divAns)

print("Transpose is : ")
transAns = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
 
print(transAns, end ='\n\n')
 
print(transAns.transpose())