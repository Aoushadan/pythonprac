class bankaccount:
    def __init__(self,accholder,balance = 0):
        self.accholder = accholder
        self._balance = balance
    def deposit(self,amount):
        if amount>0:
            self._balance = self._balance+amount
            print(f"{amount} is deposited,and my balance is {self._balance}")
        else:
            print("deposit amount is invalid")
    def check_balance(self):
        return self._balance
class savings_account(bankaccount):
    def __init__(self,accholder,balance = 0,interest_rate = 0.05):
        super().__init__(accholder,balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self._balance*self.interest_rate
        self._balance = self._balance + interest
        print(f"{interest} is calculated and my balance is {self._balance}")
savings = savings_account(accholder="Job",balance = 1000,interest_rate= 0.05)
savings.deposit(100)
savings.calculate_interest()
print(f"after savings the balance is {savings._balance}")
