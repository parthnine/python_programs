class car:
    category='suv'
    def __init__(self , modelname , year):
        self.modelname= modelname
        self.year=year
    def display(self):
        print(self.modelname , self.year)
c1= car('Nissan' , 2022)
print(c1.category)
c1.display()
