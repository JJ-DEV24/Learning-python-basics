
def diamonds_deck_of_cards_maker_dict():
    numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    diamonds = [' of Diamonds']
    diamonds_suit = {}
    for n in numbers:
        for d in diamonds:
            diamonds_suit[n] = [d]
    return diamonds_suit

print(diamonds_deck_of_cards_maker_dict())

def clubs_deck_of_cards_maker_dict():
    numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    clubs = [' of Clubs']
    clubs_suit = {}
    for n in numbers:
        for c in clubs:
            clubs_suit[n] = [c]
    return clubs_suit

print(clubs_deck_of_cards_maker_dict())

def hearts_deck_of_cards_maker_dict():
    numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    hearts = [' of Hearts']
    hearts_suit = {}
    for n in numbers:
        for h in hearts:
            hearts_suit[n] = [h]
    return hearts_suit

print(hearts_deck_of_cards_maker_dict())

def spades_deck_of_cards_maker_dict():
    numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    spades = [' of Spades']
    spades_suit = {}
    for n in numbers:
        for s in spades:
            spades_suit[n] = [s]
    return spades_suit

print(spades_deck_of_cards_maker_dict())

def special_deck_of_cards_maker_dict():
    special_numbers = {1: 'Ace', 11: 'J', 12: 'Q', 13: 'K'}
    special_numbers2 = special_numbers.values()
    suits = [' of Diamonds', ' of Hearts', ' of Spades', ' of Clubs']
    special_cards = {}
    str(n=12)
    special_cards.get(n,n)
    for x in special_numbers2:
        for s in suits:
            special_cards[x] = [s]
    return special_cards

print(special_deck_of_cards_maker_dict())

new_deck_maker_dict = {diamonds_deck_of_cards_maker_dict(), hearts_deck_of_cards_maker_dict(),
                       special_deck_of_cards_maker_dict(), spades_deck_of_cards_maker_dict(),
                       clubs_deck_of_cards_maker_dict()}

print(new_deck_maker_dict)
