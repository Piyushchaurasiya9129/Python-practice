class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposit hua. New balance: ₹{self.__balance}")
        else:
            print("Deposit amount positive hona chahiye!")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Balance kam hai, withdraw nahi ho sakta!")
        elif amount <= 0:
            print("Withdraw amount positive hona chahiye!")
        else:
            self.__balance -= amount
            print(f"{amount} withdraw hua. New balance: ₹{self.__balance}")

    def check_balance(self):
        print(f"Current balance: ₹{self.__balance}")


# Testing with menu loop
name = input("Enter your name :  ")
starting_balance = float(input("How much starting balance you want to keep :  "))
acc = BankAccount(name, starting_balance)

while True:
    print("\n--- Bank Menu ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Please enter your choice in number (1-4): ")

    if choice == "1":
        amount = float(input("How much you want to deposit : "))
        acc.deposit(amount)
    elif choice == "2":
        amount = float(input("How much you want to withdraw : "))
        acc.withdraw(amount)
    elif choice == "3":
        acc.check_balance()
    elif choice == "4":
        print("Thank you !  This session was end.")
        break
    else:
        print("Galat choice, 1-4 mein se select karo.")
