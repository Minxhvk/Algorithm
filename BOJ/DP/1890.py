import sys

def get():
    return sys.stdin.readline().rstrip()

N = int(get())

board = [list(map(int, get().split(' '))) for _ in range(N)]

# DP => 경우의 수를 cnt 한다.

dp = [[0 for _ in range(N)] for _ in range(N)]

dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if board[i][j] == 0: break
        if dp[i][j] > 0:
            cur_val = board[i][j]
            if i + cur_val < N: dp[i+cur_val][j] += dp[i][j]
            if j + cur_val < N: dp[i][j+cur_val] += dp[i][j]

print(dp[N-1][N-1])