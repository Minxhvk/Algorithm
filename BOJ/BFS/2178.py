from collections import deque
import sys


def get():
    return sys.stdin.readline().rstrip()


x, y = map(int, get().split())

board = []

for _ in range(x):
    board.append(list(map(int, input())))

dist = [[-1 for _ in range(y)] for _ in range(x)]

q = deque()

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(x):
    for j in range(y):
        if board[i][j] == 0 or dist[i][j] != -1:
            continue
        q.append([i, j])
        dist[i][j] = 1

        while len(q) > 0:
            cur = q.popleft()
            for idx in range(4):
                nx = cur[0] + dx[idx]
                ny = cur[1] + dy[idx]

                if nx >= x or ny >= y or nx < 0 or ny < 0:
                    continue
                if board[nx][ny] == 0 or dist[nx][ny] != -1:
                    continue
                dist[nx][ny] = dist[cur[0]][cur[1]] + 1
                q.append([nx, ny])

print(dist[x-1][y-1])
