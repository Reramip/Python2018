class Mortgage:
    def __init__(self, principal, interestRate, term):
        self._principal = principal
        self._interestRate = interestRate
        self._term = term

    def calculateMonthlyPayment(self):
        i = self._interestRate / 1200
        n = self._term
        A = self._principal
        monthlyPayment = A * (i / (1 - ((1 + i)**(-12 * n))))
        return monthlyPayment

class InterestOnlyMortgage(Mortgage):
    def __init__(self, principal, interestRate, term, numberOfInterestOnlyYears):
        super().__init__(principal, interestRate, term)
        self._numberOfInterestOnlyYears = numberOfInterestOnlyYears

    def initialMonthlyPayment(self):
        return self._principal*(self._interestRate/1200)

    def setTerm(self):
        self._term -= self._numberOfInterestOnlyYears

    def getTerm(self):
        return self._term

class MortgageWithPoints(Mortgage):
    def __init__(self, principal, interestRate, term, numberOfPoints):
        super().__init__(principal, interestRate, term)
        self._numberOfPoints = numberOfPoints

    def setPrincipal(self):
        self._principal *= (1 - 0.01 * self._numberOfPoints)