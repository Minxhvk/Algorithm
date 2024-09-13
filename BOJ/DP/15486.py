import sys

def get():
  return sys.stdin.readline().rstrip()

N = int(get())

dp = [0] * (N+10)
arr = [[]]

answer = -1

# Input
for _ in range(N):
  date, pay = map(int, get().split())

  arr.append([date, pay])

cur_max = 0

for i in range(1, N+1):

  cur_max = max(cur_max, dp[i])

  date, pay = arr[i]
  end_date = i + date - 1

  if (end_date) >= (N+1):
    continue

  dp[i + date] = max(cur_max + pay, dp[i + date])

print(max(dp))
