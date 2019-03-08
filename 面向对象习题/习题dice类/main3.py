import pairOfDice

def main():
    dice = pairOfDice.PairOfDice()
    count = 0
    for i in range(10000):
        dice.roll()
        if dice.sum() == 7:
            count += 1
    print("{0:.2%}".format(count/10000))

main()