import sys


def get():
    return sys.stdin.readline().rstrip()


def boom(board):
    boom = [['O' for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if board[i][j] == 'O':
                boom[i][j] = '.'
                for k in range(4):
                    cur_x = i + dx[k]
                    cur_y = j + dy[k]

                    if cur_x < 0 or cur_x >= n or cur_y < 0 or cur_y >= m:
                        continue

                    boom[cur_x][cur_y] = '.'
    return boom


n, m, target = map(int, get().split())
board = []
answer = [None for _ in range(5)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    board.append(list(get()))

answer[0] = board
first_boom = boom(board)
second_boom = boom(first_boom)


if target == 1:
    result = board
elif target % 2 == 0:
    result = [['O' for _ in range(m)] for _ in range(n)]
elif target % 4 == 3:
    result = first_boom
elif target % 4 == 1:
    result = second_boom

for i in result:
    print(''.join(i))
