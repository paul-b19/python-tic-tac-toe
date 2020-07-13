# from IPython.display import clear_output

# Starting game
def play_game():
  play = None
  while play not in ['Y', 'N']:
    play = input('Play Game? (Y / N) ').upper()
  if play == 'Y': return True
  return False

# Players selecting symbols to play X or O
def select_symbol():
  # clear_output()
  print(chr(27)+'[2j')
  print('\033c')
  print('\x1bc')
  symbol = None

  while symbol not in ['X', 'O']:
    symbol = input('Player1, please select X or O: ').upper()

  print(f'Player1 plays with {symbol}')
  if symbol == 'X': return {1:'X', 2:'O'}
  return {1:'O', 2:'X'}

# Printing game board
def display_board(board):
  # clear_output()
  print(chr(27)+'[2j')
  print('\033c')
  print('\x1bc')
  for i in board:
    print(i)

# Game move
def move(board, player):
  available = list(filter(lambda i: check_dict[i] not in ['X','O'], check_dict.keys()))
  cell = 'initial'

  while not cell.isdigit() or cell not in available:
    cell = input(f'Player {player}, please select a cell {available}: ')

    if cell.isdigit() and int(cell) in available:
      break
  
  cell = int(cell)

  for i in range(0,3):
    for j in range(0,3):
      if board[i][j] == cell: board[i][j] = player_symbol[player]
      
  check_dict[cell] = player_symbol[player]  

  display_board(board)
  
  if player == 1: player = 2
  else: player = 1

  return {'board': board, 'player': player}

# Game check (continue or game over)
def game_check(check_dict, player):
  if player == 1: player = 2
  else: player = 1
  combinations = [(1,2,3), (4,5,6), (7,8,9),
                  (1,4,7), (2,5,8), (3,6,9),
                  (1,5,9), (3,5,7)]
  for i in combinations:
    res = ''
    for j in i:
      res = res + check_dict[j]
    if res == 'XXX' or res == 'OOO':
      print(f'Player {player} won!')
      return False

  if len(list(filter(lambda i: i == '', check_dict.values()))) == 0:
    print('Nobody won! Play again!')
    return False

  return True

# GAME FLOW
while play_game():

  player = 1
  board = [[1,2,3],
           [4,5,6],
           [7,8,9]]
  player_symbol = select_symbol()
  check_dict = dict((i, '') for i in range(1,10))

  display_board(board)

  while game_check(check_dict, player):
    res = move(board, player)
    board = res['board']
    player = res['player']