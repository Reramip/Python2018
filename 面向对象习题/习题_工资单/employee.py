class Employee:
    def __init__(self, name, hours, pay):
        self._name = name
        self._hours = hours
        self._pay = pay

    def getHours(self):
        return self._hours

    def __str__(self):
        return "{0}: ${1:,.2f}".format(self._name, self.calculatePay())

class SalariedEmployee(Employee):
    def calculatePay(self):
        return self._pay

class HourlyEmployee(Employee):
    def calculatePay(self):
        return self._pay * self._hours