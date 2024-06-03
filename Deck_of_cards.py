from pprint import pprint

suits = ['diamonds', 'spades', 'hearts', 'clubs']
numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

deck_of_cards = []

for number in numbers:
    for suit in suits:
        answer = number + ' of ' + suit
        deck_of_cards.append(answer)

pprint('this is a deck of cards:')
pprint(deck_of_cards)

from random import shuffle
def card_shuffler(deck_of_cards:list):
    shuffle(deck_of_cards)
    return deck_of_cards

shuffle(deck_of_cards)
pprint(deck_of_cards)

player_1_hand = deck_of_cards.pop()

print(player_1_hand)

print(len(deck_of_cards))


# def last_name_adder(current_name, extended_name):
#     print(current_name + ' ' + extended_name)
#
#
# last_name_adder(6, 8)
# a_string:list = ''
# a_string=9
