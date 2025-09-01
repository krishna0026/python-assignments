class Account:
    def __init__(self, accno, acc_holder_name,balance):
        self.accno=accno
        self.acc_holder_name=acc_holder_name
        self.balance=balance
    def current_status_display(self):
        print(f"This account No. {self.accno} having owner {self.acc_holder_name} available balance {self.balance} Rs.")
    def diposit(self, amount):
        self.amount=amount
        print(f"Diposite of {self.amount} Rs. is successfull !!")
        self.balance = self.balance + self.amount
        print(f"This account No. {self.accno} having owner {self.acc_holder_name} updted balance {self.balance} Rs.")
    def withdraw(self, amount):
        self.amount=amount
        print(f"Withdrawl of {self.amount} Rs. is successfull !!")
        self.balance = self.balance - self.amount
        print(f"This account No. {self.accno} having owner {self.acc_holder_name} updted balance {self.balance} Rs.")


Acc1 = Account(19104910, "Krishna", 230025)
Acc1.current_status_display() # current status of account
Acc1.diposit(100000) # amount deposit
Acc1.withdraw(200000) #amount wothrwal


