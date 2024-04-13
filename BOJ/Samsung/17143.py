import sys

def get():
  return sys.stdin.readline().rstrip()

class Shark:

  def __init__(self, speed, direction, size):
    self.speed = speed
    self.direction = direction
    self.size = size

def move_shark():
  global board # 상어를 담아 놓는 board
  
  # 중복되는 상어들을 체크하기 위한 새로운 board
  temp_board = [[None for _ in range(C)] for _ in range(R)]

  for i in range(R):
    for j in range(C):
      # 상어가 없는 경우
      if board[i][j] is None: continue

      move_cnt = None
      temp_x, temp_y = i, j
      shark = board[i][j]

      # direction이 1, 2이면, (R-1) * 2를 사용한다.
      if shark.direction in [1, 2]:
        move_cnt = shark.speed % ((R-1)*2) # 계산 필요 횟수

        for _ in range(move_cnt):
          temp_x += dx[shark.direction]
		
          # 범위에서 벗어났다면, direction을 바꿔주고 
          # 잘못 연산된 +1과 -1을 바로잡기 위해 +2, -2
          if temp_x < 0:
            shark.direction = 2
            temp_x += 2 # -1 이 아닌, 1로 갔어야 하므로 +2
          if temp_x >= R:
            shark.direction = 1
            temp_x -= 2 # R이 아닌, R-2로 갔어야 하므로 -2
            
      # direction이 3, 4이면, (C-1) * 2를 사용한다.
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

      # 이미 존재하는 상어의 사이즈가 더 크다 -> 잡아 먹힘 -> 동작 X
      if temp_board[temp_x][temp_y] and temp_board[temp_x][temp_y].size > shark.size:
          continue
      
      # None 이거나, 내가 더 크므로 나로 할당한다.
      temp_board[temp_x][temp_y] = shark
    
  # 기존 board를 temp_board로 초기화.
  board = temp_board

R, C, M = map(int, get().split())
board = [[None for _ in range(C)] for _ in range(R)]
answer = 0

# direction에 따른 이동 방향
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, 1, -1]

for _ in range(M):
  x, y, s, d, z = map(int, get().split())
  x -= 1
  y -=1
  shark = Shark(s, d, z)
  board[x][y] = shark

# 시간은 필요 없고, 낚시꾼이 이동하는 경로만 체크해 주면 된다.
for i in range(C):

  # 가장 가까운 상어 찾기. == x 좌표가 가장 작은 것
  for x_idx in range(R):

    if board[x_idx][i]:
      answer += board[x_idx][i].size
      board[x_idx][i] = None
      
      break

  move_shark()
  
print(answer)