# class Account:
#     def __init__(self, accno, acc_holder_name,balance):
#         self.accno=accno
#         self.acc_holder_name=acc_holder_name
#         self.balance=balance
#     def current_status_display(self):
#         print(f"This account No. {self.accno} having owner {self.acc_holder_name} available balance {self.balance} Rs.")
#     def diposit(self, amount):
#         self.amount=amount
#         print(f"Diposite of {self.amount} Rs. is successfull !!")
#         self.balance = self.balance + self.amount
#         print(f"This account No. {self.accno} having owner {self.acc_holder_name} updted balance {self.balance} Rs.")
#     def withdraw(self, amount):
#         self.amount=amount
#         print(f"Withdrawl of {self.amount} Rs. is successfull !!")
#         self.balance = self.balance - self.amount
#         print(f"This account No. {self.accno} having owner {self.acc_holder_name} updted balance {self.balance} Rs.")


# Acc1 = Account(19104910, "Krishna", 230025)
# Acc1.current_status_display() # current status of account
# Acc1.diposit(100000) # amount deposit
# Acc1.withdraw(200000) #amount wothrwal

# print("--------------------------------------")
# print("--------------------------------------")

# Acc2 = Account(19104915, "Jatin", 1500000)
# Acc2.current_status_display() # current status of account
# Acc2.diposit(302045) # amount deposit
# Acc2.withdraw(104824) #amount wothrwal

from flask import Flask, render_template, request
import os

app = Flask(__name__, template_folder="f-end")

# ---- Account Class ----
class Account:
    def __init__(self, accno, acc_holder_name, balance):
        self.accno = accno
        self.acc_holder_name = acc_holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"✅ Deposited {amount} Rs. Updated balance: {self.balance} Rs."

    def withdraw(self, amount):
        if amount > self.balance:
            return "❌ Insufficient balance!"
        self.balance -= amount
        return f"💸 Withdrawn {amount} Rs. Updated balance: {self.balance} Rs."


# ---- Multiple Accounts ----
accounts = {
    19104910: Account(19104910, "Krishna", 230025),
    19104915: Account(19104915, "Jatin", 1500000),
    19104920: Account(19104920, "Aditi", 50000)
}


# ---- Routes ----
@app.route("/")
def home():
    return render_template("index.html", accounts=accounts, selected=None)


@app.route("/select", methods=["POST"])
def select_account():
    accno = int(request.form["accno"])
    account = accounts.get(accno)
    if not account:
        return render_template("index.html", accounts=accounts, selected=None, message="❌ Account not found!")
    return render_template("index.html", accounts=accounts, selected=account)


@app.route("/deposit", methods=["POST"])
def deposit():
    accno = int(request.form["accno"])
    account = accounts.get(accno)
    if not account:
        return render_template("index.html", accounts=accounts, selected=None, message="❌ Account not found!")

    amount = int(request.form["amount"])
    msg = account.deposit(amount)
    return render_template("index.html", accounts=accounts, selected=account, message=msg)


@app.route("/withdraw", methods=["POST"])
def withdraw():
    accno = int(request.form["accno"])
    account = accounts.get(accno)
    if not account:
        return render_template("index.html", accounts=accounts, selected=None, message="❌ Account not found!")

    amount = int(request.form["amount"])
    msg = account.withdraw(amount)
    return render_template("index.html", accounts=accounts, selected=account, message=msg)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
