# Displays tic-tac-toe board
def display_board(board):
    separator = "-" * 6

    for i in range(3):
        start = i * 3
        print(f"{board[start]}|{board[start + 1]}|{board[start + 2]}|")
        if i < 2:
            print(separator)


# Gets player input, validates
def player_input():
    acceptable_values = ["X", "O"]
    choice = input("Player 1: Do you want to be X or O? ")
    while choice not in acceptable_values:
        print("Invalid choice!")
        choice = input("Player 1: Do you want to be X or O? ")

    if choice == "X":
        print("Player 1, you will go first!")
    else:
        print("Player 1, you will go second.")
    return choice


# Takes user position, assigns to board
def place_marker(board, mark):
    choice = "wrong"
    acceptable_values = range(1, 10)
    within_range = False
    spot_free = False

    if mark == "X":
        player = 1
    else:
        player = 2

    while not spot_free:
        choice = input(f"Player {player}, enter your desired position (1-9): ")

        if not choice.isdigit():
            print("Sorry, invalid input!")
        elif int(choice) not in acceptable_values:
            print("Sorry, out of range!")
        elif board[int(choice) - 1] != " ":
            print("That spot is taken!")
        else:
            # Valid position and spot is free
            board[int(choice) - 1] = mark
            spot_free = True

    return board


# Checks for win conditions
def win_check(board, mark):
    return (
        (board[0] == board[1] == board[2] == mark)  # Top row
        or (board[3] == board[4] == board[5] == mark)  # Middle row
        or (board[6] == board[7] == board[8] == mark)  # Bottom row
        or (board[0] == board[3] == board[6] == mark)  # Left column
        or (board[1] == board[4] == board[7] == mark)  # Middle column
        or (board[2] == board[5] == board[8] == mark)  # Right column
        or (board[0] == board[4] == board[8] == mark)  # Diagonal \
        or (board[2] == board[4] == board[6] == mark)  # Diagonal /
    )


# Asks players if they want to replay the game
def replay():
    choice = "wrong"
    acceptable_values = ["Y", "N", "y", "n"]
    choice = input("Do you want to play again? (Y or N): ")
    while choice not in acceptable_values:
        print("Invalid choice!")
        choice = input("Do you want to play again? (Y or N): ")
    return choice


# Game
game_on = True

# Outer loop to allow replaying
while game_on:
    print("\n" * 100)
    print("Welcome to my Tic Tac Toe game!")
    first_time = True
    user_guesses = [" "] * 9

    if first_time:
        marker = player_input()
        first_time = False

    # Inner loop (individual match)
    while True:
        display_board(user_guesses)
        place_marker(user_guesses, marker)

        # Check for win
        if win_check(user_guesses, marker):
            display_board(user_guesses)
            print(f"Player {1 if marker == 'X' else 2} wins!")
            break  # Returns control to outer loop

        # Check for tie
        if " " not in user_guesses:
            display_board(user_guesses)
            print("It's a tie!")
            break  # Returns control to outer loop

        # Switch Player
        marker = "O" if marker == "X" else "X"

    # After a win or tie, ask to replay. One replay check
    if replay() == "y" or replay() == "Y":
        continue
    else:
        print("Thanks for playing!")
        game_on = False
