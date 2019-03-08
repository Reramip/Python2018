import pCard

def main():
    cardList=[]
    for i in range(5):
        card = pCard.PlayingCard()
        card.selectAtRandom()
        cardList.append(card)
    cardList.sort(key=lambda x: x.getRank())
    for c in cardList:
        print(c)

main()