class Account:
    # Construct an Account object
    def __init__(self, id, balance=100, annualInterestRate=0.0):
        self.id = id
        self.balance = balance
        self.annualInterestRate = annualInterestRate

    def getMonthlyInterestRate(self):
        return self.annualInterestRate / 12

    def setPreviousPrice(self, previousPrice):
        self.previousPrice = previousPrice

    def setCurrentPrice(self, currentPrice):
        self.currentPrice = currentPrice

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount  # self.balance = self.balance + amount

    def getMonthlyInterest(self):
        return self.balance * self.getMonthlyInterestRate()

def main():
    # Create an account with width 4 and height 40
    account = Account(1122, 20000, 4.5)

    account.withdraw(2500)
    account.deposit(3000)
    print("ID is", account.id)
    print("Balance is", account.balance)
    print("Monthly interest rate is", account.getMonthlyInterestRate())
    print("Monthly interest is", account.getMonthlyInterest())

main()
