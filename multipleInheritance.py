class abhijit():
    def devloper(self):
        print("Abhijit is Good Developer") 

class arijit():
	def singing(self):
		print("Arijit sings well")
		
class soham():
	def coding(self):
		print("Soham codes well")

class siddhant():
	def playing(self):
		print("Siddhant playing chess well")

class passion(abhijit, soham, siddhant, arijit):
	def play(self):
		print("Both are follow the passion")

passion = passion()

passion.devloper()
passion.singing()
passion.coding()
passion.playing()		
