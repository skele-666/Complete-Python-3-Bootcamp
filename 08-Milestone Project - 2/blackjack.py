# IMPORTS AND GLOBAL VARIABLES
import random

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
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
        # If total value > 21 and you have aces, subtract 10
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


# FUNCTIONS
def take_bet(player_chips):
    # Take bet from user with input using player_chips.total and player_chips.bet
    # Use try/except statements to validate betting

    print(f"You have {player_chips.total} chips.")

    while True:
        try:
            bet_amount = int(input("How much would you like to bet? "))
        except ValueError:
            print("That's not a valid bet!")
            continue
        except:
            print("An unexpected error occurred.")
            continue
        else:
            if bet_amount > player_chips.total:
                print(
                    f"Sorry, you don't have enough chips! You have ${player_chips.total} chips."
                )
            elif bet_amount <= 0:
                print("Bet must be greater than 0!")
            else:
                player_chips.bet = bet_amount
                print(f"You have bet {player_chips.bet} chips.")
                break


def hit(deck, hand):
    # Either player can take hits until they bust. This function will be called during gameplay anytime a Player requests a hit, or a Dealer's hand is less than 17.
    hand.add_card(deck.deal())


def hit_or_stand(deck, hand):
    # If the Player Hits, employ the hit() function above. If the Player Stands, set the playing variable to False - this will control the behavior of the while loop in the game loop
    global playing

    while True:
        choice = input("Hit or stand? (h/s): ")
        if choice.lower() == "h":
            hit(deck, hand)
            break
        elif choice.lower() == "s":
            print("Player stands. Dealer's turn.")
            playing = False
            break
        else:
            print("Sorry, please try again.")
            continue

    pass


# Show cards
def show_some(player, dealer):
    # For when the player is deciding to hit or stand
    print("Dealer's Hand:")
    print("<hidden>")
    for card in dealer.cards[1:]:
        print(card)
    print("\nPlayer's Hand:")
    for card in player.cards:
        print(card)


def show_all(player, dealer):
    print(f"Dealer's Hand (value = {dealer.value}):")
    for card in dealer.cards:
        print(card)
    print(f"\nPlayer's Hand (value = {player.value}):")
    for card in player.cards:
        print(card)


# End of game
def player_busts(player_chips):
    print("Player busts! Dealer wins.")
    player_chips.lose_bet()


def player_wins(player_chips):
    print("Player wins!")
    player_chips.win_bet()


def dealer_busts(player_chips):
    print("Dealer busts! Player wins.")
    player_chips.win_bet()


def dealer_wins(player_chips):
    print("Dealer wins!")
    player_chips.lose_bet()


def push():
    print("It's a tie! No one wins.")


def replay():
    choice = "wrong"
    acceptable_values = ["y", "n", "Y", "N"]
    while choice not in acceptable_values:
        choice = input("Do you want to play again? (y or n): ")
        if choice not in acceptable_values:
            print("Invalid choice!")
    return choice


# GAME
while True:
    # Print an opening statement
    print("Welcome to Blackjack!")
    playing = True

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
    show_some(player, dealer)

    while playing:  # recall this variable from our hit_or_stand function
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player)

        # Show cards (but keep one dealer card hidden)
        show_some(player, dealer)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player.value > 21:
            player_busts(player_chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player.value <= 21:
        while dealer.value < 17:
            hit(deck, dealer)

            # Show all cards
            show_all(player, dealer)

            if dealer.value > 21:
                dealer_busts(player_chips)
            elif player.value > dealer.value:
                player_wins(player_chips)
            elif dealer.value > player.value:
                dealer_wins(player_chips)
            else:
                push()

        # Inform Player of their chips total
        print(f"You have {player_chips.total} chips.")

        # Ask to play again
        if replay() == "y" or replay() == "Y":
            continue
        else:
            print("Thanks for playing!")
            break

# # TESTING
# if __name__ == "__main__":
#     test_card = Card("Hearts", "Ace")
#     print(test_card)  # Output: Ace of Hearts

#     test_deck = Deck()
#     print(test_deck)
#     print(f"Total cards in deck: {len(test_deck.cards)}")  #
#     print(test_deck.cards[0])

#     player = Hand()
#     player.add_card(test_deck.deal())

#     for card in player.cards:
#         print(card)

#     player_chips = Chips()
#     take_bet(player_chips)
