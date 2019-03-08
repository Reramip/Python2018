import pCard

def main():
    card = pCard.PlayingCard('2')
    while card.getRank() not in ["Jack", "Queen", "King"]:
        card.selectAtRandom()
    print(card)

main()