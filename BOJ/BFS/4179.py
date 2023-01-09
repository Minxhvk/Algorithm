from collections import deque
import sys

"""
풀이 : 불의 이동시간을 구한 뒤, 사람이 이동할 수 있는 범위를 구한다.
"""

def get():
    return sys.stdin.readline().rstrip()

x, y = list(map(int, get().split()))

board = []
fire_q = deque()
human_q = deque()

for _ in range(x):
    board.append(list(map(str, get())))

dist = [[-1 for _ in range(y)] for _ in range(x)]
dist_human = [[-1 for _ in range(y)] for _ in range(x)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(x):
    for j in range(y):
        if board[i][j] == 'J':
            human_q.append([i, j])
            dist_human[i][j] = 0
        if board[i][j] == 'F':
            fire_q.append([i, j])
            dist[i][j] = 0

# 불
while len(fire_q) > 0:
    cur = fire_q.popleft()

    for idx in range(4):
        cur_dx = cur[0] + dx[idx]
        cur_dy = cur[1] + dy[idx]

        if cur_dx >= x or cur_dx < 0 or cur_dy >= y or cur_dy < 0:
            continue
        if dist[cur_dx][cur_dy] < 0 and board[cur_dx][cur_dy] == '.':
            dist[cur_dx][cur_dy] = dist[cur[0]][cur[1]] + 1
            fire_q.append([cur_dx, cur_dy])
            
# 사람
while len(human_q) > 0 :
    cur = human_q.popleft()

    next_value = dist_human[cur[0]][cur[1]] + 1

    for idx in range(4):
        cur_dx = cur[0] + dx[idx]
        cur_dy = cur[1] + dy[idx]

        if cur_dx >= x or cur_dx < 0 or cur_dy >= y or cur_dy < 0:
            print(next_value)
            sys.exit()

        if dist_human[cur_dx][cur_dy] == -1 and board[cur_dx][cur_dy] == '.':
            if dist[cur_dx][cur_dy] != -1 and next_value >= dist[cur_dx][cur_dy]:
                continue
            dist_human[cur_dx][cur_dy] = next_value
            human_q.append([cur_dx, cur_dy])
                

print('IMPOSSIBLE')
