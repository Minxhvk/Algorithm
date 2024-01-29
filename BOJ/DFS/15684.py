import sys

def get():
  return sys.stdin.readline().rstrip()

def check_complete():

  for start in range(n):
    cur = start
    for j in range(h):
      if board[j][cur]:
        cur += 1
      elif cur > 0 and board[j][cur-1]:
        cur -= 1
    if cur != start:
      return False
    
  return True


def dfs(depth, cnt):
  global answer

  if depth == cnt:
    if check_complete():
      answer = min(answer, cnt)
    return
  
  if cnt == 3:
    return
  
  for j in range(h):
    for i in range(n-1):
      if board[j][i] or board[j][i+1] or (i >= 1 and board[j][i-1]): continue
      
      board[j][i] = True
      dfs(depth, cnt+1)
      board[j][i] = False
        


n, m, h = map(int, get().split())
board = [[False] * n for _ in range(h)]

for _ in range(m):
  a, b = map(int, get().split())
  board[a-1][b-1] = True

answer = 4

for i in range(4):
  dfs(i, 0)

print(answer if answer < 4 else -1)