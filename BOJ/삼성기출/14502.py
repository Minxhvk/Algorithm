import copy
import sys
from collections import deque


def get():
    return sys.stdin.readline().rstrip()


result = -sys.maxsize  # 최댓값을 구하기 위한 -maxsize
dx = [-1, 1, 0, 0]  # 변환 x좌표
dy = [0, 0, -1, 1]  # 변환 y좌표


def bfs(arr):

    que = deque()  # bfs 좌표 담을 deque
    temp_arr = copy.deepcopy(arr)

    rtn = 0

    for i in range(n):
        for j in range(m):
            if temp_arr[i][j] != 2:
                continue

            que.append([i, j])

    while que:
        x, y = que.popleft()

        for k in range(4):
            cur_x = x + dx[k]
            cur_y = y + dy[k]

            # Index Out Of Range
            if cur_x < 0 or cur_x >= n or cur_y < 0 or cur_y >= m:
                continue
            if temp_arr[cur_x][cur_y] != 0:
                continue

            temp_arr[cur_x][cur_y] = 2
            que.append([cur_x, cur_y])

    for i in range(n):
        for j in range(m):
            if temp_arr[i][j] == 0:
                rtn += 1

    return rtn


def search_min(cnt):

    # 벽을 3개 다 사용했을 경우
    if cnt == 3:
        global result
        result = max(result, bfs(board))  # result 갱신
        return

    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                board[i][j] = 1

                search_min(cnt + 1)  # Back Tracking

                board[i][j] = 0  # 기본 값 복원


n, m = map(int,  get().split())  # Board  Size
board = [list(map(int, get().split())) for _ in range(n)]

search_min(0)

print(result)
