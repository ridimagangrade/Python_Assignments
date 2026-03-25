class Bank:
    def __init__(self, account_number: str, account_holder: str, balance: float = 0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount: float) -> str:
        if amount > 0:
            self.balance += amount
            return f"Deposited: {amount}. New balance: {self.balance}"
        return "Deposit amount must be positive."

    def withdraw(self, amount: float) -> str:
        if amount <= 0:
            return "Withdrawal amount must be positive."
        if amount > self.balance:
            return "Insufficient funds."
        self.balance -= amount
        return f"Withdrew: {amount}. New balance: {self.balance}"

    def get_balance(self) -> str:
        return f"Current balance: {self.balance}"

    def __str__(self):
        return (f"Account Number: {self.account_number}, "
                f"Account Holder: {self.account_holder}, "
                f"Balance: {self.balance}")

# --- Test Cases ---

# 1. Vikram's Account 
account1 = Bank("AC-8822001", "Vikram Singh", 5000)
print(account1)
print(account1.deposit(1000))
print(account1.withdraw(500))
print("-" * 30)

# 2. Neha's Account
account2 = Bank("AC-9911002", "Neha Sharma") 
print(account2)
print(account2.deposit(15000)) 
print(account2.withdraw(200))
print("-" * 30)

# 3. Arjun's Account
account3 = Bank("AC-7733003", "Arjun Das", 250)
print(account3)
print(account3.withdraw(500)) 
print(account3.deposit(-50))