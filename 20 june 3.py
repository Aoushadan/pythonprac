class bankaccount:
    def __init__(self,accholder,balance = 0):
        self.accholder = accholder
        self._balance = balance
    def deposit(self,amount,currency = "USD"):
        if amount>0:
            self._balance = self._balance+amount
            print(f"{amount} is deposited,and my balance is {self._balance}")
        else:
            print("deposit amount is invalid")
    def withdraw(self,amount):
        if amount <= self._balance:
            self._balance = self._balance-amount
            print(f"{amount} is withdrawn and my balance is {self._balance}")
class savingsaccount(bankaccount):
    def __init__(self ,accholder,balance = 0,overdraftlimit = 1000):
        super().__init__(accholder,balance)
        self.overdraftlimit = overdraftlimit
    def withdraw(self,amount):
        if amount <= self._balance+self.overdraftlimit:
            self._balance = self._balance-amount
            print(f"{amount} is withdrawn and my balance is {self._balance}")
        else:
            print("Exceeded overdraft limit")
basic_acc =bankaccount("Job",1000)
basic_acc.deposit(1000)
basic_acc.deposit(2000,"INR") #METHOD OVERLOADING BY ADDING CURRENCY
sav_acc = savingsaccount("Job",balance=3000,overdraftlimit=2000)
sav_acc.withdraw(4000) #METHOD OVERRIDING BY USING SAME METHOD
sav_acc.withdraw(4000)