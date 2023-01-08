import sys
from collections import deque

y, x = map(int, sys.stdin.readline().rstrip().split())

board = []

for _ in range(x):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

dist = [[0 for _ in range(y)] for _ in range(x)]

que = deque()

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(x):
    for j in range(y):
        if board[i][j] == 1:
            que.append([i, j])
        if board[i][j] == 0:
            dist[i][j] = -1

while len(que) > 0:
    cur = que.popleft()
    for idx in range(4):
        nx = cur[0] + dx[idx]
        ny = cur[1] + dy[idx]

        if nx >= x or ny >= y or nx < 0 or ny < 0:
            continue
        if dist[nx][ny] != -1:
            continue

        dist[nx][ny] = dist[cur[0]][cur[1]] + 1
        que.append([nx, ny])

result = 0
for i in dist:
    for j in i:
        if j == -1:
            print(-1)
            sys.exit()
        if j > result:
            result = j

print(result)
