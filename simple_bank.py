accounts = {}

# Function to create a new account
def create_account():
    name = input("Enter your name: ")
    acc_no = input("Enter your account number: ")

    if acc_no in accounts:
        print("Account already exists.")
    else:
        accounts[acc_no] = {
            "name": name,
            "balance": 0,
            "transaction": []
        }
        print(f" Account created successfully for {name}!")

# Login function
def login():
    acc_no = input(" Enter your account number: ")
    if acc_no in accounts:
        print(f"Welcome {accounts[acc_no]['name']}!")
        account_menu(acc_no)
    else:
        print("Invalid account number.")

# Deposit function
def deposit(acc_no):
    amount = float(input("Enter amount to deposit: ₹"))
    if amount > 0:
        accounts[acc_no]["balance"] += amount
        add_to_history(acc_no, "Deposit", amount)
        print(f" Deposit of ₹{amount} successful.")
    else:
        print("Invalid amount.")

# Withdraw function
def withdraw(acc_no):
    amount = float(input("Enter amount to withdraw: ₹"))
    if amount > 0 and accounts[acc_no]["balance"] >= amount:
        accounts[acc_no]["balance"] -= amount
        add_to_history(acc_no, "Withdraw", amount)
        print(f" Withdrawal of ₹{amount} successful.")
    elif amount > accounts[acc_no]["balance"]:
        print("Insufficient balance.")
    else:
        print("Invalid amount.")

# Check balance
def check_balance(acc_no):
    balance = accounts[acc_no]["balance"]
    print(f"Current balance: ₹{balance}")

# Add history
def add_to_history(acc_no, type, amount):
    accounts[acc_no]["transaction"].append({
        "type": type,
        "amount": amount
    })


# Print passbook
def print_passbook(acc_no):
    print(f"Passbook for Account: {acc_no}")
    transactions = accounts[acc_no]["transaction"]
    if not transactions:
        print("🕸️ No transactions yet.")
    else:
        for entry in transactions:
            print(f"{entry['type']}: ₹{entry['amount']}")

# After login
def account_menu(acc_no):
    while True:
        print("Account Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Print Passbook")
        print("5. Logout")

        c1 = input("Enter your choice (1-5): ")

        if c1 == '1':
            deposit(acc_no)
        elif c1 == '2':
            withdraw(acc_no)
        elif c1 == '3':
            check_balance(acc_no)
        elif c1 == '4':
            print_passbook(acc_no)
        elif c1 == '5':
            print("Logged out successfully.")
            break
        else:
            print(" Invalid option.")

# welcome
def welcome():
    print(" Welcome to the Bank!")
    while True:
        print("\n Main Menu:")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        c2 = input("Enter your choice (1-3): ")

        if c2 == '1':
            create_account()
        elif c2 == '2':
            login()
        elif c2 == '3':
            print(" Thank you for banking with us!")
            break
        else:
            print(" Invalid choice.")

welcome()