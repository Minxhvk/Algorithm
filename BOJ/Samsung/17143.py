import sys
from collections import deque

def get():
  return sys.stdin.readline().rstrip()

class Shark:

  def __init__(self, x, y, speed, direction, size):
    self.x = x
    self.y = y
    self.speed = speed
    self.direction = direction
    self.size = size

def move_shark():
  global board
  
  temp_board = [[None for _ in range(C)] for _ in range(R)]

  for i in board:
    for shark in i:
      if shark is None: continue
      
      move_cnt = None

      # 처음 자기 자리로 돌아오는 경우
      if shark.direction in [1, 2]:
        move_cnt = shark.speed % ((R-1)*2)

        for i in range(move_cnt):
          shark.x += dx[shark.direction]

          if shark.x < 0:
            shark.direction = 2
            shark.x += 2
          if shark.x >= R:
            shark.direction = 1
            shark.x -= 2
      else:
        move_cnt = shark.speed % ((C-1)*2)
        for i in range(move_cnt):
          shark.y += dy[shark.direction]

          if shark.y < 0:
            shark.direction = 3
            shark.y += 2
          if shark.y >= C:
            shark.direction = 4
            shark.y -= 2

      # 이미 존재하는 상어의 사이즈가 더 큼 -> 잡아 먹힘
      if temp_board[shark.x][shark.y] and temp_board[shark.x][shark.y].size > shark.size:
          continue
          
      temp_board[shark.x][shark.y] = shark

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
  shark = Shark(x, y, s, d, z)
  board[x][y] = shark


for i in range(C):
  
  for x_idx in range(R):

    if board[x_idx][i]:
      answer += board[x_idx][i].size
      board[x_idx][i] = None
      
      break

  move_shark()
  
print(answer)