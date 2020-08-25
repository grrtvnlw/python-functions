def get_coords(player):
  y_move = int(input(f'Give me y coordinate, Player {player}: '))
  x_move = int(input(f'Give me x coordinate, Player {player}: '))
  return (y_move, x_move)

def print_board(game_board):
  print(game_board[0])
  print(game_board[1])
  print(game_board[2])

def check_win(board):
  if board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X':
    print('X Wins')
    return False
  elif board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X':
    print('X Wins')
    return False
  elif board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X':
    print('X Wins')
    return False
  elif board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X':
    print('X Wins')
    return False
  elif board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X':
    print('X Wins')
    return False
  elif board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X':
    print('X Wins')
    return False
  elif board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
    print('X Wins')
    return False
  elif board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
    print('X Wins')
    return False
  elif board[0][0] == 'Y' and board[0][1] == 'Y' and board[0][2] == 'Y':
    print('Y Wins')
    return False
  elif board[1][0] == 'Y' and board[1][1] == 'Y' and board[1][2] == 'Y':
    print('Y Wins')
    return False
  elif board[2][0] == 'Y' and board[2][1] == 'Y' and board[2][2] == 'Y':
    print('Y Wins')
    return False
  elif board[0][0] == 'Y' and board[1][0] == 'Y' and board[2][0] == 'Y':
    print('Y Wins')
    return False
  elif board[0][1] == 'Y' and board[1][1] == 'Y' and board[2][1] == 'Y':
    print('Y Wins')
    return False
  elif board[0][2] == 'Y' and board[1][2] == 'Y' and board[2][2] == 'Y':
    print('Y Wins')
    return False
  elif board[0][0] == 'Y' and board[1][1] == 'Y' and board[2][2] == 'Y':
    print('Y Wins')
    return False
  elif board[0][2] == 'Y' and board[1][1] == 'Y' and board[2][0] == 'Y':
    print('Y Wins')
    return False
  else:
    return True

def move(location, player):
  coordOne = location[0]
  coordTwo = location[1]

  if board[coordOne][coordTwo] == '':
    board[coordOne][coordTwo] = player
    print_board(board)
  else:
    print('Occupied')
    move(get_coords(player), player)

while True:
  play = input('Play tic-tac-toe? y/n ').lower()
  if play == 'y':
    board=[['', '', ''], ['', '', ''], ['', '', '']]
  while play == 'y':
    if check_win(board):
      move(get_coords('X'), 'X')
      if check_win(board):
        move(get_coords('Y'), 'Y')
      else:
        break
    else:
      break
  else:
    break