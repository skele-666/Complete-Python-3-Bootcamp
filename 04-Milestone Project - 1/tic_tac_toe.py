print('\n' * 100)

# User guesses array
user_guesses = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

# Displays tic-tac-toe board
def display_board(board):
  row = '{}|{}|{}|'
  separator = '-' * 6
  
  for i in range(3):
    start = i * 3
    print(f'{user_guesses[start]}|{user_guesses[start + 1]}|{user_guesses[start + 2]}|')
    if i < 2:
      print(separator)

display_board(user_guesses)

# Gets player input, validates
def player_input():
  choice = 'wrong'
  player = ''
  acceptable_values = ['X', 'O']
  while choice not in acceptable_values:
    choice = input('Player 1: Do you want to be X or O? ')
    if choice not in acceptable_values:
      print('Invalid choice!')
  
  if choice == 'X':
    print('Player 1, you will go first!')
    player = 1
  else:
    print('Player 1, you will go second.')
    player = 2
  return choice

player_input = player_input()

# Takes user position, assigns to board
# place_marker(user_guesses, player_input())
def place_marker(user_guesses, marker):
  choice = 'wrong'
  acceptable_values = range(9)
  within_range = False
  
  if marker == 'X':
    player = 1
    player_flag = True
  else:
    player = 2
    player_flag = False
  
  # while choice not in acceptable_values:
  #   choice = input(f'Player {player}, enter your desired position (1-9): ')
  #   if choice not in acceptable_values:
  #     print('Invalid choice!')
  
  while not choice.isdigit() or not within_range:
    choice = input(f'Player {player}, enter your desired position (1-9): ')
    if not choice.isdigit(): print('Sorry, invalid input!')
    
    if choice.isdigit():
      if int(choice) in acceptable_values:
        within_range = True
  
  choice = int(choice)
  
  if player_flag:
    user_guesses[choice - 1] = 'X'
  else:
    user_guesses[choice - 1] = 'O'
  
  return user_guesses

place_marker(user_guesses, player_input)
display_board(user_guesses)







# Game Play....
print('Welcome to Tic Tac Toe!')

