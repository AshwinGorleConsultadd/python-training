class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        print(f"Deposited ${amount:.2f}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError(f"Insufficient funds. Available balance: ${self.balance}")
        self.balance -= amount
        print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    def get_balance(self):
        print(f"Current balance: ${self.balance}")
        return self.balance


#Driver Code
print("Welcome to the Bank Account Simulator!")
name = input("Enter your name to create an account: ")
account = BankAccount(name)

while True:
    print("\n--- Menu ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == '1':
        try:
            amount = float(input("Enter amount to deposit: $"))
            account.deposit(amount)
        except ValueError as e:
            print("Error:", e)

    elif choice == '2':
        try:
            amount = float(input("Enter amount to withdraw: $"))
            account.withdraw(amount)
        except ValueError as e:
            print("Error:", e)

    elif choice == '3':
        account.get_balance()

    elif choice == '4':
        print(f"Goodbye, {account.owner}!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")


