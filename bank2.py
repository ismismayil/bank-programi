class Account:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance
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
            print(f"Account №: {account.account_number}, Owner: {account.name}, Balance: {account.balance} AZN")
        elif choice == "2":
            amount = float(input("Enter deposit amount: "))
            if amount > 0:
                account.balance += amount
                print(f"{amount} AZN added to the account. New balance: {account.balance} AZN")
            else:
                print("Invalid amount.")
        elif choice == "3":
            amount = float(input("Enter withdrawal amount: "))
            if 0 < amount <= account.balance:
                account.balance -= amount
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
