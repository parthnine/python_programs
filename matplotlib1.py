from matplotlib import pyplot as plt
names = ["Abhijit", "Soham", "Dhiraj"]
marks = [80,85,90]
plt.subplot(2,3,1)
plt.bar(names, marks, color = "r")
plt.subplot(2,3,2)
plt.scatter(names, marks, color = "g")
plt.subplot(2,3,3)
plt.plot(names, marks, color = "b")
plt.subplot(2,3,4)
plt.bar(names, marks, color = "c")
plt.subplot(2,3,5)
plt.scatter(names, marks, color = "y")
plt.subplot(2,3,6)
plt.plot(names, marks, color = "b")
plt.suptitle("Ploting Graphs in python")
plt.show()

