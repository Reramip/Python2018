class Register:
    def __init__(self):
        self._number = 0
        self._money = 0

    def add(self, vehicle):
        self._number += 1
        if (vehicle == "car"):
            self._money += 1
        else:
            self._money += 2

    def getNumber(self):
        return self._number

    def getMoney(self):
        return self._money

def main():
    condition = 'Y'
    ok = Register()
    while(condition == 'Y'):
        vehicle = input("Enter type of vehicle: ")
        ok.add(vehicle)
        print("Number of vehicles: {0}".format(ok.getNumber()))
        print("Money collected: ${0:.2f}".format(ok.getMoney()))
        condition = input("Do you want to enter more vehicles (Y/N)? ")
    print("Have a good day.")

main()