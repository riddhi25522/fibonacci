class BankAccount:
    def __init__(self, account_holder, initial_balance=0.0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def check_balance(self):
        print(f"Account balance for {self.account_holder}: ${self.balance}")


# Example usage
if __name__ == "__main__":
    # Create a new bank account
    account1 = BankAccount("John Doe", 1000.0)

    # Perform transactions
    account1.deposit(500.0)
    account1.withdraw(200.0)
    account1.check_balance()
