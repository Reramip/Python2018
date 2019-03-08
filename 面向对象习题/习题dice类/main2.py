import pairOfDice

def main():
    p1 = pairOfDice.PairOfDice()
    p2 = pairOfDice.PairOfDice()
    p1.roll()
    p2.roll()
    p1Sum = p1.sum()
    p2Sum = p2.sum()
    print("Player 1: ",p1Sum)
    print("Player 2: ",p2Sum)
    if p1Sum > p2Sum:
        print("Player 1 wins.")
    elif p1Sum == p2Sum:
        print("Tie.")
    else:
        print("Player 2 wins.")

main()