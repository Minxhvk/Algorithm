import sys

def get():
  return sys.stdin.readline().rstrip()

N, K = map(int, get().split())

arr = [list(map(int, get().split())) for _ in range(N)]

"""
dp[i][j] i : 물건 번호, j : 가방 무게
"""

arr = [[0, 0]] + arr
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

# 짐
for i in range(1, N+1):
  w, v = arr[i]
  # 무게
  for j in range(1, K+1):

    diff = j - w
    
    temp = 0
    # 들어갈 수 있음
    if diff >= 0:
      temp = dp[i-1][diff] + v

    # max(지금 넣을 수 없는 무게, 이전에 넣었던 무게 최대)
    dp[i][j] = max(temp, dp[i-1][j])

print(dp[N][K])
