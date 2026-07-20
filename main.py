from student import Student

def add_student():
	try:
		name = input("Enter your name: ")
		roll_no = int(input("Enter your roll_no: "))
		mark = int(input("Enter your mark: "))
		
		s = Student(name , roll_no , mark)
		
		with open ("students.txt" , "a") as f:
			f.write(s.student_info() + "\n")
			
		print("Student added successfully!\n")
		
	except ValueError :
		print("ERROR: please enter roll_no and marks in number")
		
		
def view_students():
	try:
		with open ("students.txt" , "r") as f:
			data = f.readlines()
			if not data:
				print("No one student here.\n")
			for line in data:
				name,roll_no,mark = line.strip().split(",")
				print(f"Name: {name}, Roll No: {roll_no}, Mark: {mark} ")
				
		print()

	except FileNotFoundError:
				print("until no one student add ")
											
while True:
	print("1. Add Student" )
	print("2. View Students")
	print("3. Exit")
	choice = input("Enter choice: ")
	
	if choice == "1":
		add_student()
	elif choice == "2":
		view_students()
	elif choice == "3":
		print("Program is ending...")
		break
	else:
		print("Wrong choice,try again.\n")