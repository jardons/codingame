VALUES = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, "A": 11
}

def GetScore(cards):
    ace_count = sum(1 for card in cards if card == 'A')
    score = sum(VALUES[card] for card in cards)

    # Blackjack is best result.
    if score == 21 and len(cards) == 2: return 22;

    while ace_count > 0 and score > 21:
        ace_count -= 1
        score -= 10

    # More than 21 always lose, no more values differences.
    if score > 21: return 0

    return score

bank_cards, player_cards = (input().split() for _ in range(2))
bank_score, player_score = GetScore(bank_cards), GetScore(player_cards)

if player_score > 0 and player_score == bank_score:
    print("Draw")
elif player_score > bank_score:
    print('Blackjack!' if player_score == 22 else 'Player')
else:
    print('Bank')
