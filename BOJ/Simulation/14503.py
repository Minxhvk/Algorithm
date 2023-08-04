import sys


def get():
    return sys.stdin.readline().rstrip()


n, m = map(int, get().split())  # board size
f_x, f_y, f_b = map(int, get().split())

board = []

if f_b == 1 or f_b == 3:
    f_b = int((f_b+2) % 4)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for i in range(n):
    board.append(list(map(int, get().split(' '))))

result = 0

while True:
    if board[f_x][f_y] == 0:
        board[f_x][f_y] = 2
        result += 1

    dust_flag = 0
    for i in range(1, 5):
        cur_b = int((f_b+i) % 4)  # div(4)로 방향 판단

        cur_x = f_x + dx[cur_b]
        cur_y = f_y + dy[cur_b]

        if board[cur_x][cur_y] == 0:
            f_x = cur_x
            f_y = cur_y
            f_b = cur_b
            break

        else:
            dust_flag += 1

    if dust_flag == 4:
        f_x = f_x + dx[int((f_b+2) % 4)]
        f_y = f_y + dy[int((f_b+2) % 4)]

        if board[f_x][f_y] == 1:
            break

print(result)
