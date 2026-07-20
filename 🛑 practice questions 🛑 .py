	#🛑 practice questions 🛑 

'''1. Class & Object Basics
Student class banao jisme __init__ se name, roll_no, marks set ho. Ek method display() bhi ho jo details print kare. 2 students ka object bana ke test karo.

2. Encapsulation
ATM class banao jisme __pin (private) aur __balance (private) ho. Methods:
check_balance(pin) — pin match ho tabhi balance dikhaye
withdraw(pin, amount) — pin match ho aur balance sufficient ho tabhi paise nikaale
@property use karke balance ko read-only expose karo.

3. Inheritance
Vehicle parent class banao (brand, speed attributes, info() method). Fir Car aur Bike child classes banao jo Vehicle ko inherit kare aur apna extra attribute add kare (jaise Car me doors, Bike me has_gear).

4. Polymorphism
Teen classes banao — Cat, Dog, Cow — sabme ek sound() method ho jo alag-alag print kare ("Meow", "Woof", "Moo"). Fir ek list me sabke objects daal ke loop se sabka sound() call karo (yehi polymorphism dikhata hai).

5. Abstraction (ABC)
Ek abstract class Shape banao (ABC module use karke) jisme abstract method area() ho. Fir Circle aur Rectangle classes banao jo isse inherit kare aur apna area() implement kare. Object try karo Shape ka directly — dekho error kyu aata hai.

6. Mixed (thoda tricky)
Employee (parent) → Manager aur Developer (child) banao. Encapsulation use karo __salary ke liye, ek abstract method work() rakho parent me, aur har child apna work() implement kare (polymorphism). Ye ek chhota mini-project jaisa hai — sab concepts ek saath.

class Student :
	def __init__ (self, name , roll_no):
		self.name = name 
		self.roll_no = roll_no
		
	def show_detail (self):
		return f"This is {self.name} and his roll number is : {self.roll_no}"

s1 = Student("Piyush" , 34)
print(s1.show_detail())
	
	
	
class ATM :
	def __init__(self, pin , balance):
		self.__pin = pin
		self.__balance = balance
		
				
	def check_balance(self , pin):
		if pin == self.__pin:
			print(f"your balance is : {self.__balance}")
		
		elif pin != self.__pin:
			print("WRONG PIN ! access denied")
	
	
	def withdraw (self , pin, amount):
		if pin != self.__pin:
			print("WRONG PIN ! access denied")
	
		elif amount > self.__balance:
			print(" sufficient balance")
			
		else:
			self.__balance -= amount
			print("withdraw successful your current balance is :{self.__balance}")	
			
		
	
	@property
	def balance (self):
		return self.__balance
				
		

cus1 = ATM("piyush", 5000)

cus1.check_balance("piyush")
cus1.withdraw("piyush", 2000)
cus1.check_balance("piyush")

print(cus1.balance)	
	
	
	
	

class Vehicle:
	def __init__(self, brand , speed):
		self.brand = brand
		self.speed = speed
		
	def get_info(self):
		return f"{self.brand} {self.speed}"
		
		
class Car(Vehicle):
	def __init__ (self, brand , speed, model):
		super().__init__(brand, speed)
		self.model = model
		
class Bike(Vehicle):
	def __init__(self, brand , speed , gear):
		super().__init__(brand, speed)
		self.gear = gear
	
p1 = Car("Tata" , 200 , "S")
print(p1.model)
print(p1.brand)
print(p1.speed)
print(p1.get_info())

p2 = Bike("Kawasaki" , 400 , 5)
print(p2.brand)
print(p2.speed)
print(p2.gear)										
p3 = Vehicle("toyota" , 500)
print(p3.get_info())	
	
	
	
	
	
class Dog:
	def __init__ (self , legs):
		self.legs = legs
		
	def sound (self):
		return "Bhow"
			
class Cat:
	def __init__(self , colour):
		self.colour = colour
		
	def sound (self):
		return "Meow"
		
			
class Cow:
	def __init__ (self, milk_ltr):
		self.milk_ltr = milk_ltr
		
	def sound (self):
		return "Moo"
							
dog1 = Dog(4)
cat1 = Cat("black")
cow1 = Cow(2)

sound = [dog1.sound() , cat1.sound() , cow1.sound()]

for i in sound:
	print(i)		
	
													


from abc import ABC,abstractmethod

class Shape(ABC):
	@abstractmethod
	def area (self):
		pass
				
class Circle(Shape):
	def __init__ (self , radius):
		self.radius = radius
		
	def area (self):
		return 3.14 * self.radius * self.radius

class Rect (Shape):
	def __init__ (self , length , breadth):
		self.length = length
		self.breadth = breadth 
		
	def area (self):
		return self.length * self.breadth

											
cir1 = Circle(5)
print(cir1.area())

rec1 = Rect(4,5)
print(rec1.area())



from abc import ABC, abstractmethod

class Employee(ABC) :
	def __init__(self , salary):
		self.__salary = salary
		
	def show_salary(self):
		return self.__salary		

	@abstractmethod
	def work(self):
 		pass
		
class Manager(Employee):
		def __init__ (self, salary , grade):
			super().__init__(salary)
			self.grade = grade
			
		def work (self):
			return "Managing team...."
				
class Developer(Employee):
			def __init__(self, salary,grade):
				super().__init__(salary)
				self.grade = grade
				
			def work (self):
				return "working..."
									
m1 = Manager(25000 , "manager")
print(m1.show_salary())	
print(m1.work())	

d1 = Developer(40000, "senior")
print(d1.show_salary())
print(d1.work())

	'''	
						
			



