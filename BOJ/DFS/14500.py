import sys

def get():
  return sys.stdin.readline().rstrip()


def dfs(x, y, temp_value, cnt):
  global answer

  # 시간 초과 최적화 ...
  if answer >= temp_value + max_pos * (4-cnt): return False
  
  if cnt == 4:
    answer = max(answer, temp_value)
    return True

  for k in range(4):
    di = x + dx[k]
    dj = y + dy[k]

    if di < 0 or di >= n or dj < 0 or dj >= m or visited[di][dj]:
      continue

    if cnt == 2:
      visited[di][dj] = True
      dfs(x, y, temp_value + arr[di][dj], cnt+1)
      visited[di][dj] = False

    visited[di][dj] = True
    dfs(di, dj, temp_value + arr[di][dj], cnt+1)
    visited[di][dj] = False


n, m = map(int, get().split())
arr = [list(map(int, get().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
answer = 0
max_pos = max(map(max, arr))

for i in range(n):
  for j in range(m):
    visited[i][j] = True
    dfs(i, j, arr[i][j], 1)
    visited[i][j] = False

print(answer)

