class student:
   def input(self , name , roll , PNR , address):
       self.name= name
       self.roll=roll
       self.PNR= PNR
       self.address = address
   def display(self):
       print("Name:" , self.name)
       print("roll" , self.roll)
       print("PNR" , self.PNR)
       print("Address" , self.address)

class CSE(student , student1 , student2):
    def setMarks(self , marks):
        self.marks = marks
    def setSubject(self , subject):
        self.subject = subject
    def display(self):
       print("Name:" , self.name)
       print("roll" , self.roll)
       print("PNR" , self.PNR)
       print("Address" , self.address)
       print("Marks:" , self.marks)
       print("Subject" , self.subject)
s1=CSE()

s3=CSE()
s1.input("Jay" , 30 , "EN21162792" , 'Satara')
s2.input("Jay" , 30 , "EN21162792" , 'Satara')
s3.input("Jay" , 30 , "EN21162792" , 'Satara')
s1.setMarks(200)
s1.setSubject("Python")
s1.display()
s2.setMarks(200)
s2.setSubject("Python")
s2.display()
s3.setMarks(200)
s3.setSubject("Python")
s3.display()
    
