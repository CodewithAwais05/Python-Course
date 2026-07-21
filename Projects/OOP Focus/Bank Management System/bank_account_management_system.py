# Bank Account Management System

class Accounts:

    def __init__(self, name, account_no, balance):

        self.name = name
        self.account_no = account_no
        self.balance = balance
        self.transaction_history = []


    def withdraw(self, amount):

        if amount <= 0:
            print("Invalid amount!")
            return

        if amount <= self.balance:

            self.balance -= amount

            print("Withdrawal Successful!!!")

            self.transaction_history.append(
                f"Withdrawn: {amount}"
            )

        else:

            print("Insufficient Balance!!!")


    def deposit(self, amount):

        if amount > 0:

            self.balance += amount

            print("Deposit Successful!!!")

            self.transaction_history.append(
                f"Deposited: {amount}"
            )

        else:

            print("Invalid amount!")


    def show_balance(self):

        print("\n------ ACCOUNT DETAILS ------")

        print("Name: ", self.name)
        print("Account Number: ", self.account_no)
        print("Current Balance: ", self.balance)


    def show_history(self):

        print("\n------ TRANSACTION HISTORY ------")

        if not self.transaction_history:

            print("No Transaction History!!")

            return

        for transaction in self.transaction_history:

            print(transaction)



# ---------------- FILE FUNCTIONS ---------------- #

def save_data(account):

    file = open("account.txt", "w")

    file.write(account.name + "\n")

    file.write(account.account_no + "\n")

    file.write(str(account.balance) + "\n")


    history = "|".join(account.transaction_history)

    file.write(history)


    file.close()



def load_data():

    try:

        file = open("account.txt", "r")


        name = file.readline().strip()

        account_no = file.readline().strip()

        balance = float(file.readline().strip())


        account = Accounts(
            name,
            account_no,
            balance
        )


        history = file.readline().strip()


        if history:

            account.transaction_history = history.split("|")


        file.close()


        return account


    except FileNotFoundError:

        return None



# ---------------- MAIN PROGRAM ---------------- #

account = load_data()


if account is None:

    print("\nCreate New Account")

    name = input("Enter Account Holder Name: ")

    account_no = input("Enter Account Number: ")

    balance = float(input("Enter Initial Balance: "))


    account = Accounts(
        name,
        account_no,
        balance
    )


    account.transaction_history.append(
        f"Account Created: {balance}"
    )



while True:


    print("\n===== BANK MANAGEMENT SYSTEM =====")

    print("1. Deposit Money")

    print("2. Withdraw Money")

    print("3. Show Balance")

    print("4. Transaction History")

    print("5. Save Data")

    print("6. Exit")


    choice = input("Enter Choice: ")



    if choice == "1":

        amount = float(input("Enter Amount to Deposit: "))

        account.deposit(amount)



    elif choice == "2":

        amount = float(input("Enter Amount to Withdraw: "))

        account.withdraw(amount)



    elif choice == "3":

        account.show_balance()



    elif choice == "4":

        account.show_history()



    elif choice == "5":

        save_data(account)

        print("Data Saved Successfully!")



    elif choice == "6":

        save_data(account)

        print("Data Saved Successfully!")

        print("Thank You!")

        break



    else:

        print("Invalid Choice!")