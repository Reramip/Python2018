import pCard

def main():
    card = pCard.PlayingCard('2', 'Clubs')
    while card.getSuit() != "Diamonds":
        card.selectAtRandom()
    print(card)

main()