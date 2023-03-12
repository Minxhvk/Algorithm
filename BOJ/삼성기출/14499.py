import sys

def get():
    return sys.stdin.readline().rstrip()

N, M, X, Y, num = map(int, get().split())

board = [list(map(int, get().split())) for _ in range(N)]

dice = [0, 0, 0, 0, 0, 0, 0]

def rotate(arr, val):
    if val == 1:
        return [0, arr[4], arr[2], arr[1], arr[6], arr[5], arr[3]]
    elif val == 2:
        return [0, arr[3], arr[2], arr[6], arr[1], arr[5], arr[4]]
    elif val == 3:
        return [0, arr[5], arr[1], arr[3], arr[4], arr[6], arr[2]]
    else:
        return [0, arr[2], arr[6], arr[3], arr[4], arr[1], arr[5]]

for command in list(map(int, get().split())):
    if command == 1:
        if Y+1 >= M: continue
        Y += 1
    elif command == 2:
        if Y-1 < 0: continue
        Y -= 1

    elif command == 3:
        if X-1 < 0: continue
        X -= 1

    elif command == 4 :
        if X + 1 >= N: continue
        X += 1

    dice = rotate(dice, command)

    if board[X][Y] == 0:
            board[X][Y] = dice[6]
    else :
      dice[6] = board[X][Y];
      board[X][Y] = 0;

    print(dice[1])