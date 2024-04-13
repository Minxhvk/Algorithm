import sys
from collections import deque

def get():
  return sys.stdin.readline().rstrip()

class Shark:

  def __init__(self, speed, direction, size):
    self.speed = speed
    self.direction = direction
    self.size = size

def move_shark():
  global board
  
  temp_board = [[None for _ in range(C)] for _ in range(R)]

  for i in range(R):
    for j in range(C):
      # 상어가 없는 경우
      if board[i][j] is None: continue

      move_cnt = None
      temp_x, temp_y = i, j
      shark = board[i][j]

      # 처음 자기 자리로 돌아오는 경우
      if shark.direction in [1, 2]:
        move_cnt = shark.speed % ((R-1)*2)

        for _ in range(move_cnt):
          temp_x += dx[shark.direction]

          if temp_x < 0:
            shark.direction = 2
            # -1 이 아닌, 1로 갔어야 하므로 +2
            temp_x += 2
          if temp_x >= R:
            shark.direction = 1
            temp_x -= 2
      else:
        move_cnt = shark.speed % ((C-1)*2)
        for _ in range(move_cnt):
          temp_y += dy[shark.direction]

          if temp_y < 0:
            shark.direction = 3
            # -1 이 아닌, 1로 갔어야 하므로 +2
            temp_y += 2
          if temp_y >= C:
            shark.direction = 4
            temp_y -= 2

      # 이미 존재하는 상어의 사이즈가 더 큼 -> 잡아 먹힘
      if temp_board[temp_x][temp_y] and temp_board[temp_x][temp_y].size > shark.size:
          continue
          
      temp_board[temp_x][temp_y] = shark

  board = temp_board

R, C, M = map(int, get().split())
board = [[None for _ in range(C)] for _ in range(R)]
answer = 0
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, 1, -1]

for _ in range(M):
  x, y, s, d, z = map(int, get().split())
  x -= 1
  y -=1
  shark = Shark(s, d, z)
  board[x][y] = shark


for i in range(C):
  
  for x_idx in range(R):

    if board[x_idx][i]:
      answer += board[x_idx][i].size
      board[x_idx][i] = None
      
      break

  move_shark()
  
print(answer)