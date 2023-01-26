import sys

n = int(sys.stdin.readline().rstrip())

board = [None for _ in range(1000002)]

board[1] = 0

for i in range(2, n+1):
    board[i] = board[i-1] + 1
    if i % 2 == 0:
        board[i] = min(board[i], board[int(i/2)]+1)
    if i % 3 == 0:
        board[i] = min(board[i], board[int(i/3)]+1)

print(board[n])
