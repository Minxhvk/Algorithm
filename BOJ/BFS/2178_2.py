import sys
from collections import deque


def get():
    return sys.stdin.readline().rstrip()


n, m = map(int, get().split())

board = [list(map(int, get())) for _ in range(n)]
dist = [[0 for _ in range(m)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque([[0, 0]])
dist[0][0] = 1

while len(q) > 0:
    cur = q.popleft()

    for k in range(4):
        cur_x = cur[0] + dx[k]
        cur_y = cur[1] + dy[k]

        if cur_x < 0 or cur_x >= n or cur_y >= m or cur_y < 0:
            continue
        if board[cur_x][cur_y] == 0 or dist[cur_x][cur_y]:
            continue

        dist[cur_x][cur_y] = dist[cur[0]][cur[1]] + 1
        q.append([cur_x, cur_y])

print(dist[n-1][m-1])
