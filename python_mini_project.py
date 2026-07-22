 	 #🛑 Mini project🛑
 		 
 	#1️⃣guess the number 👇

print("="*35) 	 	
print("Guess the number between 1 to 100")
print("="*35)	
import random
target = random.randint(1,100)
while True:
	userChoice = input ("Guess the target or Quit : ")
	if (userChoice == "Quit"):
		break
	userChoice = int(userChoice) 
	if(userChoice == target):
		print("success : Correct guess !!")
		break
	elif(userChoice<target):
		print("your number was too small. Take a bigger guess.. ")
	else:
		print("your number was too big. Take smaller guess.. ")
		
print("-----GAME OVER-----")



#2️⃣Random Paasword Generator👇

	# Method 1 👇 



import random 
import string 

pass_len = 12
charvalues = string.ascii_letters + string.digits + string.punctuation
password = ""
for i in range(pass_len):
	password += random.choice(charvalues)
	
print("your random password is :" , password)

		
		# Method 2 👇 
		
		
import random 
import string 

pass_len = 6
charvalues = string.ascii_letters + string.digits + string.punctuation
password = "" . join([random.choice(charvalues) for i in range(pass_len)])

	
print("your random password is :" , password)
