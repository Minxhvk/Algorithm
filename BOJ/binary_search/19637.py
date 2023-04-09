import sys

# 목표 : O( NlongN )

def get():
    return sys.stdin.readline().rstrip()

n, m = map(int, get().split())

board = []

for _ in range(n):
    name, val = get().split(' ')
    val = int(val)

    if board and val == board[-1][0]:
        continue
    
    board.append([name, val])

target = [int(get()) for _ in range(m)]

for val in target:
    left = 0
    right = len(board) - 1

    while left <= right:
        mid = (left + right) // 2
        if val > board[mid][1]:
            left = mid + 1
        else:
            right = mid -1

    print(board[right+1][0])