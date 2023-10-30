str=input("Enter string: ")
list1=[]
count=0
length=0
for j in str:
    length=length+1
    if j=='a' or j=='e' or j=='i' or j=='o' or j=='u' or j=='A' or j=='E' or j=='I' or j=='O' or j=='U':
        count=count+1
        list1.append(j)
print(list1)
print("Count of Vowels is: ",count)
print("Length of string is: ",length)
    