# Displays tic-tac-toe board
def display_board(board):
  row = '{}|{}|{}|'
  separator = '-' * 6
  
  for i in range(3):
    start = i * 3
    print(f'{board[start]}|{board[start + 1]}|{board[start + 2]}|')
    if i < 2:
      print(separator)

# Gets player input, validates
def player_input():
  choice = 'wrong'
  acceptable_values = ['X', 'O']
  while choice not in acceptable_values:
    choice = input('Player 1: Do you want to be X or O? ')
    if choice not in acceptable_values:
      print('Invalid choice!')
  
  if choice == 'X':
    print('Player 1, you will go first!')
  else:
    print('Player 1, you will go second.')
  return choice

# Takes user position, assigns to board
def place_marker(board, mark):
  choice = 'wrong'
  acceptable_values = range(1, 10)
  within_range = False
  spot_free = False
  
  if mark == 'X':
    player = 1
  else:
    player = 2
  
  while not spot_free:
    while not choice.isdigit() or not within_range:
      choice = input(f'Player {player}, enter your desired position (1-9): ')
      if not choice.isdigit():
        print('Sorry, invalid input!')
      elif int(choice) not in acceptable_values:
        print('Sorry, out of range!')
      else:
        within_range = True
  
    choice = int(choice)
    
    if board[choice - 1] == ' ': # If the spot is free
      spot_free = True
      if player == 1:
        board[choice - 1] = 'X'
      else:
        board[choice - 1] = 'O'
    else:
      print('That spot is taken!')
      # Reset choice loop
      choice = 'wrong'
      within_range = False
  
  return board

# Checks for win conditions
def win_check(board, mark):
  return (
        (board[0] == board[1] == board[2] == mark) or  # Top row
        (board[3] == board[4] == board[5] == mark) or  # Middle row
        (board[6] == board[7] == board[8] == mark) or  # Bottom row
        (board[0] == board[3] == board[6] == mark) or  # Left column
        (board[1] == board[4] == board[7] == mark) or  # Middle column
        (board[2] == board[5] == board[8] == mark) or  # Right column
        (board[0] == board[4] == board[8] == mark) or  # Diagonal \
        (board[2] == board[4] == board[6] == mark)     # Diagonal /
  )
    

# Asks players if they want to replay the game
def replay():
  choice = 'wrong'
  acceptable_values = ['Y', 'N']
  while choice not in acceptable_values:
    choice = input('Do you want to play again? (Y or N): ')
    if choice not in acceptable_values:
      print('Invalid choice!')
  return choice


# Game
game_on = True

# Outer loop to allow replaying
while game_on:
  print('\n' * 100)
  print('Welcome to my Tic Tac Toe game!')
  first_time = True
  user_guesses = [' '] * 9
  
  if first_time:
    current_marker = player_input()
    first_time = False
  
  # Inner loop (individual match)
  while True:
    display_board(user_guesses)
    place_marker(user_guesses, current_marker)
    
    # Check for win
    if win_check(user_guesses, current_marker):
      display_board(user_guesses)
      print(f'Player {1 if current_marker == 'X' else 2} wins!')
      break # Returns control to outer loop
      
    # Check for tie
    if ' ' not in user_guesses:
      display_board(user_guesses)
      print("It's a tie!")
      break # Returns control to outer loop
    
    # Switch Player
    current_marker = 'O' if current_marker == 'X' else 'X'
    
  # After a win or tie, ask to replay. One replay check
  if replay() == 'Y':
    continue
  else:
    print("Thanks for playing!")
    game_on = False