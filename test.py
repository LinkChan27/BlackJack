import random as rnd


def generator():
    cardnum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    card1 = rnd.choice(cardnum)
    card2 = rnd.choice(cardnum)
    return card1, card2


cards = generator()
print(cards)
