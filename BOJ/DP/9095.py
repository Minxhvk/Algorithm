import sys


def get():
    return sys.stdin.readline().rstrip()


n = int(get())
input_board = []

for _ in range(n):
    input_board.append(int(get()))

first_board = [None for _ in range(15)]
first_board[0] = 1
first_board[1] = 2
first_board[2] = 4

for i in range(3, 15):
    first_board[i] = sum(first_board[i-3:i])

for i in input_board:
    print(first_board[i-1])
