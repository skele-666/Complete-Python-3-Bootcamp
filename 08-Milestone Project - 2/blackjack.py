# IMPORTS AND GLOBAL VARIABLES
import random

suits = suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = (
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Jack",
    "Queen",
    "King",
    "Ace",
)
values = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 11,
}

playing = True


# CLASS DEFINITIONS
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[self.rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = []

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value
        if card.rank == "Ace":
            self.aces += 1

        self.adjust_for_ace()

    def adjust_for_ace(self):
        # If total value > 21 nd you have aces, subtract 10
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:

    def __init__(self):
        self.total = (
            100  # This can be set to a default value or supplied by a user input
        )
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


# FUNCTIONS
def take_bet(player_chips):
    # take bet from user with input using player_chips.total and player_chips.bet
    # Use try/except statements to validate betting

    print(f"You have {player_chips.total} chips.")

    while True:
        try:
            bet_amount = int(input("How much would you like to bet? "))
        except ValueError:
            print("That's not a valid bet!")
        else:
            if bet_amount > player_chips.total:
                print(
                    f"Sorry, you don't have enough chips! You have ${player_chips.total} chips."
                )
            elif bet_amount <= 0:
                print("Bet must be greater than 0!")
            else:
                player_chips.bet = int(bet_amount)
                print(f"You have bet {player_chips.bet} chips.")
                break


def hit(deck, hand):
    # Either player can take hits until they bust. This function will be called during gameplay anytime a Player requests a hit, or a Dealer's hand is less than 17. It should take in Deck and Hand objects as arguments, and deal one card off the deck and add it to the Hand. You may want it to check for aces in the event that a player's hand exceeds 21.
    pass

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    pass

# Show cards
def show_some(player,dealer):
    
    pass
    
def show_all(player,dealer):
    
    pass

# End of game
def player_busts():
    pass

def player_wins():
    pass

def dealer_busts():
    pass
    
def dealer_wins():
    pass
    
def push():
    pass


# GAME
while True:
    # Print an opening statement
    print("Welcome to blackjack!")

    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player = Hand()
    dealer = Hand()
    for x in range(2):
        player.add_card(deck.deal())
        dealer.add_card(deck.deal())

    # Set up the Player's chips
    player_chips = Chips()

    # Prompt the Player for their bet
    take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)

    while playing:  # recall this variable from our hit_or_stand function
        # Prompt for Player to Hit or Stand

        # Show cards (but keep one dealer card hidden)

        # If player's hand exceeds 21, run player_busts() and break out of loop

        break

        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17

        # Show all cards

        # Run different winning scenarios

        # Inform Player of their chips total

        # Ask to play again

        break


# TESTING
if __name__ == "__main__":
    test_card = Card("Hearts", "Ace")
    print(test_card)  # Output: Ace of Hearts

    test_deck = Deck()
    print(test_deck)
    print(f"Total cards in deck: {len(test_deck.cards)}")  #
    print(test_deck.cards[0])

    player = Hand()
    player.add_card(test_deck.deal())

    for card in player.cards:
        print(card)

    player_chips = Chips()
    take_bet(player_chips)
