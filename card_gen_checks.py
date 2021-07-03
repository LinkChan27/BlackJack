import random as rnd

ace = 0
card_num = [2, 3, 4, 5, 6, 7, 8, 9, 10, ace]
card1 = rnd.choice(card_num)
card2 = rnd.choice(card_num)
dcard1 = rnd.choice(card_num)
dcard2 = rnd.choice(card_num)
hand = [card1, card2]
dhand = [dcard1, dcard2]


def acecheck(i):
    if ace in i:
        if i[0] + i[1] <= 10:
            val = i.index(int('0'))
            new_ace = 11
            i.pop(val)
            i.append(new_ace)
        else:
            val = i.index(int('0'))
            new_ace = 1
            i.pop(val)
            i.append(new_ace)
    else:
        pass

    return i


def hit(h):
    new_card = rnd.choice(card_num)
    h.append(new_card)
    new = acecheck(h)
    return new


def stand(h):
    new_dhand = hit(dhand)
    dtotal = new_dhand[0] + new_dhand[1] + new_dhand[2]
    try:
        total = h[0] + h[1] + h[2]
        print(total)
    except:
        total = h[0] + h[1]
        print(f"{total} is your total\n{dtotal} is The Dealer's")

    if total < 21:
        if total > dtotal:
            print(f"You win! You got closer to 21 than The Dealer!\nThe Dealer's hand was {dtotal}")
        elif total == dtotal:
            print('Wow, that is rare, both of your points are the same. No points awarded, start over.')
        else:
            if dtotal <= 21:
                print(f"You lost, The Dealer was closer to 21 than you.\nThe Dealer's hand was {dtotal}")
            else:
                print(f"You win! The Dealer went over 21!\nThe Dealer's hand was {dtotal}")
    elif total > 21:
        print('You are over 21! You lost.')
