from card_gen_checks import *

# Cards: 2-10 are their face values, Jack-King are 10 each, Ace is either 1 or 11 (depends on your hand)
# Both players get 2 cards, dealer only shows one of their cards (other is face down)
# The goal is to get closer to 21 than the dealer without going over
# dealer only gets to hit once (?)
# if the player wins: They get the same amount as their bet if player looses: they loose their entire bet. if player pushes: nothing
# if you are dealt an ace and a 10 value card then you have a black jack and if the dealer doesnt also have a black jack then you win automatically
# Black jacks are paid 3:2 meaning that they are paid 150% of their bet
# The player can hit or stand depending on whether they feel close enough to 21 or not

print(f'Your hand is: {card1}, and {card2}\nTotal: {card1 + card2}')
hit_stand = input('Hit (1) or stand (2):\n')

if hit_stand == '1':
    new_hand = hit(hand)
    print(new_hand)
    stand(new_hand)

elif hit_stand == '2':
    stand(hand)

else:
    print('Too big of a number.')
