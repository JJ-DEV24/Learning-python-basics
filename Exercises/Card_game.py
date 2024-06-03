# Create a card game called higher or lower.
'''This game requires 2 players and there are 5 rounds. Each player has 5 cards. Each player takes a card from the top of
 their stack and whoever has the highest number gets a point.'''
from Deck_of_cards import card_shuffler

# Play
"""Create a for loop that loops over 5 time (5 rounds) and selects which player has the highest card for each round.
The player with the highest card wins a point"""


def deck_maker():
    numbers = [int('Ace'), 2, 3, 4, 5, 6, 7, 8, 9, 10, int('J'), int('Q'), int('K')]
    suits = [' of Diamonds', ' of Hearts', ' of Spades', ' of Clubs']
    new_deck_of_cards = {}
    for n in numbers:
        for s in suits:
            ans = {n + s}
            new_deck_of_cards.append(ans)
    return new_deck_of_cards

deck_of_cards = deck_maker()

card_shuffler(deck_of_cards)

for r in range(5):
        player_1 = [deck_of_cards.pop()]
        return player_1



        player_2 = [deck_of_cards.pop()]

def higher_or_lower(a,b):

    for r in range(5):
        p1_card = player_1.pop()
        p2_card = player_2.pop()
        p1_points = 0
        p2_points = 0
        if p1_card > p2_card:
                p1_points +=1
                print(f"Player 1's card is {p1_card}. Player 2's card is {p2_card}.")
                print('Player 1 wins!')
                print(f"GWARN Player 1!! Player 1 has {p1_points} points. Player 2 has {p2_points} points.")
        elif p1_card < p2_card:
                p2_points += 1
                print(f"Player 1's card is {p1_card}. Player 2's card is {p2_card}.")
                print('Player 2 wins!')
                print(f"OKAY Player 2!! Player 2 has {p2_points} points. Player 1 has {p1_points} points.")
        else:
                p1_card == p2_card
                print(f"Player 1's card is {p1_card}. Player 2's card is {p2_card}.")
                print('It\'s a tie!')
                print(f"Better luck next time guys! Player 1 has {p1_points} points. Player 2 has {p2_points} points.")


higher_or_lower(player_1, player_2)
