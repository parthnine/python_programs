class student:
    def input(self, name, rollNo, PNR, adderess):
        self.name = name
        self.rollNo = rollNo
        self.PNR = PNR
        self.adderess = adderess

    def display(self):
        print("Name : ", self.name)
        print("RollNo : ", self.rollNo)
        print("PNR : ", self.PNR)
        print("Adderess : ", self.adderess)

class CSE(student):
    def setMarks(self, marks):
        self.marks = marks
    def setSubject(self, subject):
        self.subject = subject

    def display(self):
        print("Name : ", self.name)
        print("RollNo : ", self.rollNo)
        print("PNR : ", self.PNR)
        print("Adderess : ", self.adderess) 
        print("Marks : ", self.marks)
        print("Subject : ", self.subject)


s1 = CSE()
s1.input("Abhijit", 42, "EN098765", "Kolhapur")
s1.setMarks(75)
s1.setSubject("Python Programming")
s1.display()                     