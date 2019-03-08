import pairOfDice

def main():
    dice = pairOfDice.PairOfDice()
    count10k = 0
    for i in range(10000):
        count24 = 0
        for j in range(24):
            dice.roll()
            if(dice.sum() == 12):
                count24 += 1
        if count24 > 0:
            count10k += 1
    print("{0:.2%}".format(count10k/10000))

main()