import sys


def get():
    return int(sys.stdin.readline().rstrip())


n = get()
board = []
arr = [[0 for _ in range(3)] for _ in range(n+1)]

for _ in range(n):
    board.append(get())
if n == 1:
    print(board[0])
    exit()
arr[1][1] = board[0]
arr[2][1] = board[1]
arr[2][2] = board[0] + board[1]

for i in range(3, n+1):
    arr[i][1] = max(arr[i-2][1], arr[i-2][2]) + board[i-1]
    arr[i][2] = arr[i-1][1] + board[i-1]

print(max(arr[n][1], arr[n][2]))
