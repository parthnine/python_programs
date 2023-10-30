class person:
    def __init__ (self,name,id):
        self.name = name
        self.id = id
    def display(self):
        print(self.name)
        print(self.id)

class emp(person):
    def __init__ (self,name,id,salary,post):
        #super(emp, self) . __init__(name,id)
        self.salary = salary
        self.post = post

        person.name = name
        person.id = id

    def details(self):
        print("Name: ", self.name)
        print("Id : ", self.id)
        print("Salary : ", self.salary)
        print("Post : ", self.post)

a = emp("Abhijit", 7, 20000, "Developer")

a.display()
a.details()