import mortgage

def main():
    principal = eval(input("Enter principal of mortgage: "))
    interestRate = eval(input("Enter percent interest rate: "))
    term = eval(input("Enter duration of mortgage in years: "))
    ans = mortgage.Mortgage(principal, interestRate, term)
    print("Monthly payment: ${0:,.2f}".format(ans.calculateMonthlyPayment()))

main()