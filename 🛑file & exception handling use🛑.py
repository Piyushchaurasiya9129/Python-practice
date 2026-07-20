def add_marks():
    name = input("Student ka naam: ")
    while True:
        try:
            marks = int(input("Marks: "))
            break
        except ValueError:
            print("Sirf number daalo!")
    
    with open("marks.txt", "a") as file:
        file.write(f"{name}: {marks}\n")
    print("Save ho gaya!")


def show_marks():
    try:
        with open("marks.txt", "r") as file:
            print("\n--- Sab Students ka Data ---")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("marks.txt abhi tak bani nahi hai")


# Main program
while True:
    add_marks()
    show_marks()
    
    again = input("\nAur ek student add karna hai? (yes/no): ")
    if again.lower() != "yes":
        break

print("Program band ho raha hai. Bye!")