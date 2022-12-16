import numpy as np
import random
import time

def create_board(N, M, Q, K):
  board = np.zeros((N,M))
  if Q > 0 and K > 0:
    board, remaining_knights = place_queens(board, Q, K)
    if remaining_knights > 0:
      board = place_knights(board, remaining_knights)
  else:
    if Q > 0:
      board, _ = place_queens(board, Q, K)
    else:
      board = place_knights(board, K)
  return board

def place_queens(board, Q, K):
  N = board.shape[0]
  M = board.shape[1]
  placed_queens = 0
  knight_placed = 0
  if Q <= N:
    pos_increase = round(N/Q)
    prev_pos = 0
    curr_row = 0
    while(placed_queens < Q):
      curr_pos = random.randint(0, M-1)
      while(curr_pos == prev_pos or board[curr_row][curr_pos] != 0):
          curr_pos = random.randint(0, M-1)
      board[curr_row][curr_pos] = 1
      if knight_placed < K-2:
        if curr_row + 1 < N:
          if curr_pos + 1 < M and board[curr_row + 1][curr_pos + 1] == 0:
            board[curr_row + 1][curr_pos + 1] = 2
            knight_placed+=1
          if curr_pos - 1 >= 0 and board[curr_row + 1][curr_pos - 1] == 0:
            board[curr_row + 1][curr_pos - 1] = 2
            knight_placed+=1
      prev_pos = curr_pos
      curr_row = (curr_row + pos_increase) % N
      placed_queens+=1
  elif Q <= M:
    prev_pos = 0
    curr_col = 0
    pos_increase = round(M/Q)
    while(placed_queens < Q):
      curr_pos = random.randint(0, N-1)
      while(curr_pos == prev_pos or board[curr_pos][curr_col] != 0):
          curr_pos = random.randint(0, N-1)
      board[curr_pos][curr_col] = 1
      if knight_placed < K-2:
        if curr_col + 1 < M:
          if curr_pos + 1 < N and board[curr_pos + 1][curr_col + 1] == 0:
            board[curr_pos + 1][curr_col + 1] = 2
            knight_placed+=1
          if curr_pos - 1 >= 0 and board[curr_pos - 1][curr_col + 1] == 0:
            board[curr_pos - 1][curr_col + 1] = 2
            knight_placed+=1
      prev_pos = curr_pos
      curr_col = (curr_col + pos_increase) % M
      placed_queens+=1  
  else:
    while(placed_queens < Q):
       row_pos = random.randint(0, N-1)
       col_pos = random.randint(0, M-1)
       if board[row_pos][col_pos] == 0:
         board[row_pos][col_pos] = 1
         placed_queens+=1
  return board, K-knight_placed


def place_knights(board, K):
  N = board.shape[0]
  M = board.shape[1]
  placed_knights = 0
  while(placed_knights < K):
      row_pos = random.randint(0, N-1)
      col_pos = random.randint(0, M-1)
      if board[row_pos][col_pos] == 0:
        board[row_pos][col_pos] = 2
        placed_knights+=1
  return board

def go_right_queen(board, row, col):
  N = board.shape[0]
  M = board.shape[1]
  while(col < M):
     if board[row][col]==0:
       col+=1
     elif board[row][col]==2:
       return False
     else:
       return True
  return False

def go_left_queen(board, row, col):
  N = board.shape[0]
  M = board.shape[1]
  while(col >= 0):
     if board[row][col]==0:
       col-=1
     elif board[row][col]==2:
       return False
     else:
       return True
  return False

def go_up_queen(board, row, col):
  N = board.shape[0]
  M = board.shape[1]
  while(row >= 0):
     if board[row][col]==0:
       row-=1
     elif board[row][col]==2:
       return False
     else:
       return True
  return False


def go_down_queen(board, row, col):
  N = board.shape[0]
  M = board.shape[1]
  while(row < N):
     if board[row][col]==0:
       row+=1
     elif board[row][col]==2:
       return False
     else:
       return True
  return False

def go_right_up_queen(board, row, col):
  N = board.shape[0]
  M = board.shape[1]
  while(row >= 0 and col < M):
     if board[row][col]==0:
       row-=1
       col+=1
     elif board[row][col]==2:
       return False
     else:
       return True
  return False

def go_right_down_queen(board, row, col):
  N = board.shape[0]
  M = board.shape[1]
  while(row < N and col < M):
     if board[row][col]==0:
       row+=1
       col+=1
     elif board[row][col]==2:
       return False
     else:
       return True
  return False


def go_left_up_queen(board, row, col):
  N = board.shape[0]
  M = board.shape[1]
  while(row >= 0 and col >= 0):
     if board[row][col]==0:
       row-=1
       col-=1
     elif board[row][col]==2:
       return False
     else:
       return True
  return False

def go_left_down_queen(board, row, col):
  N = board.shape[0]
  M = board.shape[1]
  while(row < N and col >= 0):
     if board[row][col]==0:
       row+=1
       col-=1
     elif board[row][col]==2:
       return False
     else:
       return True
  return False


def count_queen_attack(board, row, col):
  attack_count = 0
  if go_right_queen(board, row, col+1):
    attack_count+=1
  if go_left_queen(board, row, col-1):
    attack_count+=1
  if go_up_queen(board, row-1, col):
    attack_count+=1
  if go_down_queen(board, row+1, col):
    attack_count+=1
  if go_right_up_queen(board, row-1, col+1):
    attack_count+=1
  if go_right_down_queen(board, row+1, col+1):
    attack_count+=1
  if go_left_up_queen(board, row-1, col-1):
    attack_count+=1
  if go_left_down_queen(board, row+1, col-1):
    attack_count+=1
  return attack_count

def count_knight_attack(board, row, col):
# row and colom of knights current position
  N = board.shape[0]
  M = board.shape[1]
  attack_count = 0
  if(row+1 < N and col+2 < M):
    if board[row+1][col+2]!=0:
      attack_count+=1
  if(row-1 >= 0 and col+2 < M):
    if board[row-1][col+2]!=0:
      attack_count+=1
  if(row+1 < N and col-2 >= 0):
    if board[row+1][col-2]!=0:
      attack_count+=1
  if(row-1 >=0 and col-2 >= 0):
    if board[row-1][col-2]!=0:
      attack_count+=1
  if(row+2 < N and col+1 < M):
    if board[row+2][col+1]!=0:
      attack_count+=1
  if(row-2 >= 0 and col+1 < M):
    if board[row-2][col+1]!=0:
      attack_count+=1
  if(row+2 < N and col-1 >= 0):
    if board[row+2][col-1]!=0:
      attack_count+=1
  if(row-2 >=0 and col-1 >= 0):
    if board[row-2][col-1]!=0:
      attack_count+=1
  return attack_count

def get_total_attack(board):
  total_attack = 0
  N = board.shape[0]
  M = board.shape[1]
  for row in range(N):
    for col in range(M):
      if board[row][col] == 1:
        total_attack+=count_queen_attack(board, row, col)
      elif board[row][col] == 2:
        total_attack+=count_knight_attack(board, row, col)
  return total_attack

def convert_to_representation(item):
  if item == 1:
    return 'Q'
  if item == 2:
    return 'K'
  return 'E'