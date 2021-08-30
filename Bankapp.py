import sys
class Bank:
    Bank_name = "Python Bank"
    def __init__(self,name,surname,bal=0.0):
        self.name=name
        self.surname=surname
        self.bal=bal
    def deposite(self,amount):
        self.bal=self.bal+amount
        print("Balance after deposit amount:{}".format(self.bal))
    def withdraw(self,amount):
        if amount>self.bal or amount==0:
            print("Insufficiant Fund")
            return
        self.bal=self.bal-amount
        print("Balance after witdraw:{}".format(self.bal))
    def checkBal(self):
        print("Your balance is:{}".format(self.bal))

print("Wellcome to Python Bank App")
name=input("Enter your name:")
surname=input("Enter your surname:")
print("Bank name:{}".format(Bank.Bank_name))
obj = Bank(name,surname)

while True:
    print(" 1.d-Deposit \n 2.w-Withdraw \n 3.c-Check Balance \n 4.e-Exit")
    choice = int(input("Enter your choice"))
    if choice==1:
        amount=float(input("Enter amount:"))
        obj.deposite(amount)
    elif choice==2:
        amount=float(input("Enter amount:"))
        obj.withdraw(amount)
    elif choice==3:
        obj.checkBal()
    elif choice==4:
        sys.exit()
    else:
        print("Please enter valid choice:")







