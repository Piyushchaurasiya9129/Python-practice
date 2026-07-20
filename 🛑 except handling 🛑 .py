	#🛑 exception handling 🛑
'''	
a = input("enter a number : ")
print(f"multiplication table of {a} is : ")
try :
	for i in range (1, 11):
		print(f"{int(a)} × {i} = {int(a)*i}")
		
except:
	print("Invalid input")
	
	
print("hii sab thik thak")
print("aur sab thik hi hai ")

#👉 mtlb try lagane se agar error aayega to wah except me jo print krne ko kahega wah print ho jayega aur aage ka program chal jayega error nhi aayega 



	#🛑finally ka use 👇
	
def func1():	
	try :
		n = [1, 5, 7, 8]
		i = int(input("Enter the index: "))
		print(n[i])
		return 1
		
	except :
		print("Some error occurred")
		return 0
		
	finally :
		print("I am always executed")

x = func1()
print(x)	


#👉 finally aur except hamesa execute honge aur finally chahe error aaye yaa simple chal jaye hamesha execute hoga 




		#🛑 raise custom error 👇
		
		
a = int(input("Enter a number between 5 and 9 :  "))

if a < 5 or a > 9:
	raise ValueError("Value should be between 5 and 9")
	

#👉 iska use isiliye hota hai taki kahi user galat value de to program wahi ruk jaye uske wajah se aage ka program kharab na ho

'''

	#🛑 practice 👇
	
	
try:
	a = int(input("Enter a divide number: "))
	b = int(input("Enter a number divide by: "))
	
	result = a / b
	#print(result)
except ValueError as e:
	print(e)
	print("please enter only int value")
	
except ZeroDivisionError as e:
	print(e)
	print("You can't divide by zero Idiot!")

except Exception as e:
	print(e)
	print("Something went wrong")
	
else:
	print(result)