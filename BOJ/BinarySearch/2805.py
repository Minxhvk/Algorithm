# H를 이분 탐색으로 계산한다.
# 매개변수 탐색

import sys

def get():
  return sys.stdin.readline().rstrip()

n, m = map(int, get().split())
arr = list(map(int, get().split()))
arr.sort()
start, end = 1, arr[-1]

while start <= end:
  mid = (start + end) // 2
  tree = 0

  for i in range(n-1, -1, -1):
    if arr[i] > mid:
      tree += arr[i] - mid
    else:
      break

  if tree >= m:
    start = mid + 1
  else:
    end = mid - 1

print(end)
      

