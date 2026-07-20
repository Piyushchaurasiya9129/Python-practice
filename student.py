class Student :
	def __init__ (self, name , roll_no , mark):
		self.name = name 
		self.roll_no = roll_no
		self.__mark = mark
		
	def get_mark(self):
		return self.__mark
		
	def student_info(self):
		return f"{self.name} , {self.roll_no} , {self.__mark}"
		
	
