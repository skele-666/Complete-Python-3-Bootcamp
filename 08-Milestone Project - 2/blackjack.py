# IMPORTS AND GLOBAL VARIABLES
import random

suits = suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {
  'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
  'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11
}

playing = True

# CLASS DEFINITIONS
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[self.rank]
    
    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck:
    def __init__(self):
        self.cards = [];
        
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank));
    
    def shuffle(self):
        random.shuffle(self.all_cards)
    
    def deal(self):
        return self.all_cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
    
    def add_cards(self, new_cards):
        if isinstance(new_cards, list):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def __str__(self):
        return f'{self.name} has {len(self.all_cards)} cards.'

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self, card):
        pass
    
    def adjust_for_ace(self):
        pass




# GAME SETUP
# player_one = Player("One")
# player_two = Player("Two")

# new_deck = Deck()
# new_deck.shuffle()

# # Give two cards to each player
# for x in range(4):
#     player_one.add_cards(new_deck.deal())
#     player_two.add_cards(new_deck.deal())

      

# TESTING
if __name__ == "__main__":
    test_card = Card('Hearts', 'Ace')
    print(test_card)  # Output: Ace of Hearts
    
    test_deck = Deck()
    print(test_deck)
    print(f'Total cards in deck: {len(test_deck.cards)}')  #
    print(test_deck.cards[0])
