class SavingsAccount:
    def __init__(self, name="", balance=0):
        self._name = name
        self._balance = balance

    def getBalance(self):
        return self._balance

    def makeDeposit(self, deposit):
        self._balance += deposit

    def makeWithdrawal(self, withdrawal):
        self._balance -= withdrawal

def main():
    name = input("Enter person's name: ")
    print("D = Deposit, W = Withdrawal, Q = quit")
    condition = 'A'
    account = SavingsAccount(name)
    while condition != 'Q':
        condition = input("Enter D, W, or Q: ").upper()
        if condition == 'D':
            deposit = eval(input("Enter amount to deposit: "))
            account.makeDeposit(deposit)
            print("Balance: ${0:,.2f}".format(account.getBalance()))
        elif condition == 'W':
            withdrawal = eval(input("Enter amount to withdraw: "))
            if withdrawal > account.getBalance():
                print("Insufficient funds, transaction denied.")
            else:
                account.makeWithdrawal(withdrawal)
                print("Balance: ${0:,.2f}".format(account.getBalance()))
    print("End of transactions. Have a good day", name + '.')

main()