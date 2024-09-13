import sys
from collections import deque

def get():
  return sys.stdin.readline().rstrip()

def bfs(cur_num):

  if len(arr[cur_num]) <= 0:
    return 1
  
  q = deque()
  q.append(cur_num)
  visited = [False] * (N+1)
  cnt = 1

  while q:
    cur = q.popleft()
    visited[cur] = True
    for i in arr[cur]:
      if visited[i] == True: continue

      visited[i] = True
      cnt += 1
      q.append(i)

  return cnt


N, M = map(int, get().split())

arr = [[] for _ in range(N+1)]

max_cnt = -1
answer = []

for _ in range(M):
  a, b = map(int, get().split())

  arr[b].append(a)

for i in range(N+1):
  cnt = bfs(i)

  if cnt > max_cnt:
    answer = [str(i)]
    max_cnt = cnt
  elif cnt == max_cnt:
    answer.append(str(i))
    
print(*answer)