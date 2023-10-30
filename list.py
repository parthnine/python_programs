# List Program
l1 = [1,2,"Hello",3.4]

print(type(l1))
print (l1[0:])
print(l1[:])
print(l1[2:4])
print(l1[:4])
print(l1[:-1])
print(l1[-3:-1])

l1[2] = 10;
print(l1)
l1[3:4]=[89,36]
print(l1)

#Repetion
l2 = l1*2
print(l2)

#Concatenation
l3 = l1+l2;
print(l3)
print(len(l3))

#Ierating
for i in l3 :
    print(i)
    
#Membership
print(1 in l1)
