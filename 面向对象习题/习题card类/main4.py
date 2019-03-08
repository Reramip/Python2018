import pCard

def main():
    cardList = []
    for i in range(13):
        card=pCard.PlayingCard()
        card.selectAtRandom()
        cardList.append(card)
    cardList.sort(key=lambda x: x.getSuit(), reverse=True)
    for c in cardList:
        print(c)

main()
