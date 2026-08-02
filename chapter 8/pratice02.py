class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    # Debit
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")

    # Credit
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")

    # Balance
    def get_balance(self):
        print("Total Balance:", self.balance)


acc1 = Account(10000, 20000)

acc1.debit(1000)
acc1.credit(500)
acc1.get_balance()