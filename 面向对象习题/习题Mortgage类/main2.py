import mortgage

def main():
    principal = eval(input("Enter principal of mortgage: "))
    interestRate = eval(input("Enter percent interest rate: "))
    term = eval(input("Enter duration of mortgage in years: "))
    numberOfInterestOnlyYears = eval(input("Enter number of interst-only years: "))
    theMortgage = mortgage.InterestOnlyMortgage(principal, interestRate, term, numberOfInterestOnlyYears)
    if term <= numberOfInterestOnlyYears:
        print("Monthly payment of first {0:d} years: ${1:,.2f}".format(term, theMortgage.calculateMonthlyPayment()))
    else:
        payment = theMortgage.calculateMonthlyPayment()
        print("Monthly payment for first {0:d} years: ${1:,.2f}".format(numberOfInterestOnlyYears, payment))
        theMortgage.setTerm()
        payment = theMortgage.calculateMonthlyPayment()
        print("Monthly payment for last {0:d} years: ${1:,.2f}".format(theMortgage.getTerm(), payment))

main()