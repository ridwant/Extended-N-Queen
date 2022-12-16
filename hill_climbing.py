import numpy as np
import random
import time

from board_helper import (
    create_board,
    get_total_attack
)

def simple_hill_climbing(N, M, Q, K, start_time, tmax):
  board = create_board(N, M, Q, K)
  minimum_attack = get_total_attack(board)
  while(time.time() - start_time < tmax):
    if minimum_attack == 0:
      return board
    queen_tuples = np.where(board == 1)
    queen_positions = list(zip(queen_tuples[0], queen_tuples[1]))
    knights_tuples = np.where(board == 2)
    knight_positions = list(zip(knights_tuples[0], knights_tuples[1]))
    occupied_positions = queen_positions + knight_positions
    random.shuffle(occupied_positions)
    for position in occupied_positions:
      row = position[0]
      col = position[1]
      position_init_value = board[row][col]
      range_M = [x for x in range(M) if x != col]
      random.shuffle(range_M)
      new_col = col
      for col_index in range_M:
        col_index = random.choice(range_M)
        board[row][col] = board[row][col_index]
        board[row][col_index] = position_init_value
        attack_count = get_total_attack(board)
        if attack_count <= minimum_attack:
          minimum_attack = attack_count
          new_col = col_index
        board[row][col_index] = board[row][col]
        board[row][col] = position_init_value
      
      board[row][col] = board[row][new_col]
      board[row][new_col] = position_init_value
      if minimum_attack == 0:
        return board

  return board