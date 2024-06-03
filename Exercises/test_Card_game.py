from unittest import TestCase

"""
Player 1's card is 2 of Hearts. Player 2's card is 7 of Hearts. -Player 2 wins 🥳
Player 2 wins!
Player 1's card is K of Diamonds. Player 2's card is 3 of Spades. - Player 1 wins 🥳
Player 1 wins!
Player 1's card is Ace of Spades. Player 2's card is Q of Spades. - Player 2 wins 🥳
Player 2 wins!
Player 1's card is K of Spades. Player 2's card is 10 of Hearts. - Player 1 wins 🥳
Player 1 wins!
Player 1's card is 5 of Spades. Player 2's card is 5 of Clubs. - Tie 🧐
Player 1 wins!
"""
from Card_game import deck_maker


class Test(TestCase):
    def test_tie_rules_for_higher_or_lower(self):
        my_deck_of_cards = deck_maker()
        test_card_1 = my_deck_of_cards.index('5 of Spades')
        print(f"This is test card {test_card_1}.")
        print(len(my_deck_of_cards))
