import random
import datetime
class Account:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance
        self.card_number = self.generate_card_number()  
        self.cvv = self.generate_cvv() 
        self.expiration_date = self.generate_expiration_date() 
        self.transaction_history = []
    def generate_card_number(self):
        return "".join([str(random.randint(0, 9)) for _ in range(16)])  
    def generate_cvv(self):
        return "".join([str(random.randint(0, 9)) for _ in range(3)])  
    def generate_expiration_date(self):
        current_year = datetime.datetime.now().year
        expiration_year = random.randint(current_year, current_year + 5)  
        expiration_month = random.randint(1, 12)  
        return f"{expiration_month:02d}/{expiration_year}"  
    def add_transaction(self, transaction_type, amount):
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transaction_history.append({
            "date": date,
            "transaction_type": transaction_type,
            "amount": amount,
            "balance_after": self.balance
        })
    def show_account_details(self):
        print(f"Account №: {self.account_number}, Owner: {self.name}, Balance: {self.balance} AZN")
        print(f"Card Number: {self.card_number}, CVV: {self.cvv}, Expiration Date: {self.expiration_date}")
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(f"{transaction['date']} - {transaction['transaction_type']} - Amount: {transaction['amount']} AZN - Balance: {transaction['balance_after']} AZN")
bank = {}
def register():
    username = input("Enter your name: ")
    password = input("Create a password: ")
    if username in bank:
        print("This account already exists. Please log in.")
        return None
    while True:
        account_number = input("Enter your desired account number: ")
        if account_number in [account.account_number for account in [user["account"] for user in bank.values()]]:
            print("This account number is already taken. Please choose another one.")
        else:
            break
    bank[username] = {"password": password, "account": Account(account_number, username)}
    print(f"Registration successful for {username}. Your account number is {account_number}.")
def login():
    username = input("Enter your name: ")
    password = input("Enter your password: ")
    if username in bank and bank[username]["password"] == password:
        print(f"Welcome back, {username}!")
        return bank[username]["account"]
    else:
        print("Invalid username or password. Try again.")
        return None
def account_operations(account):
    while True:
        print("\nWelcome to the Bank System")
        print("1. Show Account Details")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            account.show_account_details()
        elif choice == "2":
            amount = float(input("Enter deposit amount: "))
            if amount > 0:
                account.balance += amount
                account.add_transaction("Deposit", amount)
                print(f"{amount} AZN added to the account. New balance: {account.balance} AZN")
            else:
                print("Invalid amount.")
        elif choice == "3":
            amount = float(input("Enter withdrawal amount: "))
            if 0 < amount <= account.balance:
                account.balance -= amount
                account.add_transaction("Withdraw", amount)
                print(f"{amount} AZN withdrawn. New balance: {account.balance} AZN")
            else:
                print("Invalid amount or insufficient funds.")
        elif choice == "4":
            receiver = input("Enter receiver's account number: ")
            if receiver in [acc.account_number for acc in [user["account"] for user in bank.values()]]:
                amount = float(input("Enter transfer amount: "))
                if 0 < amount <= account.balance:
                    account.balance -= amount
                    for user in bank.values():
                        if user["account"].account_number == receiver:
                            user["account"].balance += amount
                            account.add_transaction("Transfer", amount)
                            user["account"].add_transaction("Received Transfer", amount)
                            print(f"{amount} AZN transferred to {receiver}.")
                            break
                else:
                    print("Transfer failed due to insufficient funds or invalid amount.")
            else:
                print("Receiver account not found.")
        elif choice == "5":
            print("Exiting the system...")
            break
        else:
            print("Invalid choice! Please enter a valid number.")
while True:
    print("\nWelcome to the Bank System")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")
    if choice == "1":
        register()
    elif choice == "2":
        account = login()
        if account:
            account_operations(account)
    elif choice == "3":
        print("Exiting the system...")
        break
    else:
        print("Invalid choice! Please enter a valid number.")

