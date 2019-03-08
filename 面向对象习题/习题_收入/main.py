class Wages:
    def __init__(self, name, time, pay):
        self._name = name
        self._time = time
        self._pay = pay

    def payForWeek(self):
        if self._time > 40:
            sumwage = self._pay * 40 + self._pay * 1.5 *(self._time-40)
        else:
            sumwage = self._pay * self._time
        return sumwage

def main():
    name = input("Enter person's name: ")
    time = eval(input("Enter number of hours worked: "))
    pay = eval(input("Enter hourly wage: "))
    sumwage = Wages(name, time, pay).payForWeek()
    print("Pay for", name + ": ${0:.2f}".format(sumwage))

main()