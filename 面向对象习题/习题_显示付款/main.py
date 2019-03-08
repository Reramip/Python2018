class Purchase:
    def __init__(self, describe, price, number):
        self._describe = describe
        self._price = price
        self._number = number

    def getDescribe(self):
        return self._describe

    def getPrice(self):
        return self._price

    def getNumber(self):
        return self._number

class Cart:
    def __init__(self):
        self._goods = []

    def addGoods(self, good):
        self._goods.append(good)

    def showInfo(self):
        print("{0:<10s}{1:<6s}{2:>10s}".format("ARTICLE", "PRICE", "QUANTITY"))
        sumPrice = 0
        for i in range(len(self._goods)):
            describe = self._goods[i].getDescribe()
            price = self._goods[i].getPrice()
            number = self._goods[i].getNumber()
            sumPrice += price * number
            print("{0:<10s}${1:<5.2f}{2:^12d}".format(describe, price, number))
        print("\nTOTAL COST: $" + "{0:.2f}".format(sumPrice))

def main():
    condition = 'Y'
    buy = Cart()
    while(condition == 'Y'):
        describe = input("Enter description of article: ")
        price = eval(input("Enter price of article: "))
        number = int(input("Enter quantity of article: "))
        article = Purchase(describe, price, number)
        buy.addGoods(article)
        condition = input("Do you want to enter more articles (Y/N)? ")
    buy.showInfo()

main()