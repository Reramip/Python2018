import pairOfDice

def main():
    dice=pairOfDice.PairOfDice()
    dice.roll()
    print("Red die: ", dice.getRedDie())
    print("Blue die: ", dice.getBlueDie())
    print("Total: ", dice.sum())

main()