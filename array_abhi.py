import array as arr

a = arr.array('i', [10,20,30])

for i in range(0,3):
    print(a[i], end=" ")

print()

a1 = arr.array('d', [2,5,3,5,6,1])
for i in range(0,3):
    print(a[i], end=" ")

print()

a.insert(1,4)
for i in range(0,4):
    print(a[i], end=" ")

print()

a.append(50)
for i in range(0,5):
    print(a[i], end=" ")

print()

a.pop()
for i in range(0,4):
    print(a[i], end=" ")

print()