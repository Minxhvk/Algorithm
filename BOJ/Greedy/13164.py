import sys

get = lambda: sys.stdin.readline().rstrip()

N, K = map(int, get().split())

arr = list(map(int, get().split()))

board = []

for i in range(N-1, 0, -1):
    board.append(arr[i]-arr[i-1])

board = sorted(board)

print(sum(board[:N-K]))

