t1=(1,3,2,4,5,7,8)
l1=[]
l2=[]
for i in t1:
    if i%2==0:
        l1.append(i)
    else:
        l2.append(i)
print("Even Numbers are: ",l1)
print("Odd Numbers are: ",l2)