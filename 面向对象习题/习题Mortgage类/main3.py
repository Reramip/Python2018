import mortgage

def main():
    principal = eval(input("Enter principal of mortgage: "))
    interestRate = eval(input("Enter percent interest rate: "))
    term = eval(input("Enter duration of mortgage in years: "))
    numberOfPoints = eval(input("Enter number of discount points: "))
    mort = mortgage.MortgageWithPoints(principal, interestRate, term, numberOfPoints)
    print("Monthly payment: ${0:,.2f}".format(mort.calculateMonthlyPayment()))

main()