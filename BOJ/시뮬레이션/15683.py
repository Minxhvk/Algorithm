import copy
import sys


def get():
    return sys.stdin.readline().rstrip()


n, m = map(int, get().split())

board_1 = []
board_2 = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
cctv = []
cnt = 0

for _ in range(n):
    board_1.append(list(map(int, get().split())))

for i in range(n):
    for j in range(m):
        cur = board_1[i][j]

        if cur not in [0, 6]:
            cctv.append([i, j])
        if cur == 0:
            cnt += 1


def OOB(a, b):
    return a < 0 or a >= n or b < 0 or b >= m


def upd(x, y, dir):

    dir %= 4

    while (True):
        x += dx[dir]
        y += dy[dir]

        if OOB(x, y) or board_2[x][y] == 6:
            return 0
        if board_2[x][y] != 0:
            continue

        board_2[x][y] = 7


for tmp in range(4 ** len(cctv)):
    board_2 = copy.deepcopy(board_1)

    brute = tmp

    for i in range(len(cctv)):
        dir = int(brute % 4)
        brute /= 4

        x = cctv[i][0]
        y = cctv[i][1]

        cur = board_1[x][y]
        if cur == 1:
            upd(x, y, dir)
        elif cur == 2:
            upd(x, y, dir)
            upd(x, y, dir+2)
        elif cur == 3:
            upd(x, y, dir)
            upd(x, y, dir+1)
        elif cur == 4:
            upd(x, y, dir)
            upd(x, y, dir+1)
            upd(x, y, dir+2)
        else:
            upd(x, y, dir)
            upd(x, y, dir+1)
            upd(x, y, dir+2)
            upd(x, y, dir+3)
    val = 0
    for i in board_2:
        val += i.count(0)

    cnt = min(cnt, val)

print(cnt)
