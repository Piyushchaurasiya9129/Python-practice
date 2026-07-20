# 🛑 File handling 🛑

#mode : r - read, w - write, a - append 

'''#open file
file = open("example.txt" , "r")

#🛑read file
file = open("example.txt" , "r")
content = file.read() # read entire data
print(content)
file.close() # best practice


#🛑readline file
file = open("example.txt" , "r")
content = file.readline() # read first line
print(content)
file.close()


#🛑readlines file
file = open("example.txt" , "r")
content = file.readlines() # list entire data
print(content)
file.close() 


#🛑write to a file 

file = open("example2.txt" , "w") #write mode

#note👉 example2.txt file nhi tha lekin jab write ka use kiye to wah apne aap create kar diya 

file = open("example2.txt" , "w")
file.write("Namastey, yahi se write kar rha hu")
file.close()

#🛑append mode

file = open("example2.txt" , "a") # append mode 
file.write("\nBadhiya hai ")
file.close()


# 🛑 close a file
# using with statement 

with open("example2.txt" , "r") as file:
	content = file.read()
	print(content)



#🛑 Koi file delete ke liye 👇 

import os

os.remove("example.txt")

'''




