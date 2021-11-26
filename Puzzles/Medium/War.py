import sys
import math

def draw():
    card = input()[0:-1]
    if card == 'J': return 11
    if card == 'Q': return 12
    if card == 'K': return 13
    if card == 'A': return 14
    return int(card)

# Load card value and remove their
hand1 = [draw() for i in range(int(input()))]
hand2 = [draw() for i in range(int(input()))]

round, bet1, bet2 = 0, [], []

while hand1 and hand2:
    card1, card2 = hand1.pop(0), hand2.pop(0)
    bet1.append(card1); bet2.append(card2)

    if card1 == card2:
        if len(hand1) < 4 or len(hand2) < 4:
            round = -1
            break
        
        bet1.extend(hand1[0:3]); bet2.extend(hand2[0:3])
        hand1, hand2 = hand1[3:], hand2[3:]
        continue
    
    round += 1
    winner = hand1 if card1 > card2 else hand2

    winner.extend(bet1)
    winner.extend(bet2)
    bet1, bet2 = [], []

print("PAT" if round == -1 else f'{1 if hand1 else 2} {round}')
