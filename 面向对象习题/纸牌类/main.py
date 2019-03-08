import random

class Card:
    def __init__(self, rank='', suit=''):
        self._rank = rank
        self._suit = suit

    def selectAtRandom(self):
        ranks=['2', '3', '4', '5', '6', '7', '8', '9', "10", "Jack", "Queen", "King", "Ace"]
        self._rank = random.choice(ranks)
        self._suit = random.choice(["Spades", "Hearts", "Clubs", "Diamonds"])

    def __str__(self):
        return (self._rank + " of " + self._suit)

def main():
    c=Card() 
    c.selectAtRandom()
    print(c)

main()