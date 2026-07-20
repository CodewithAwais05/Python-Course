class Account:

    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no
    
    def debit(self, amount):
        self.balance -= amount
        print(amount, " debited!!!")
    
    def credit(self, amount):
        self.balance += amount
        print(amount, " credited!!!")
    
    def total_balance(self):
        print("Total Balance:  ", self.balance)
    

a1 = Account(50000, 12345678)
a1.debit(5300)
a1.credit(543.7392)
a1.total_balance()