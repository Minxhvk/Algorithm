# 예산을 이분탐색으로 탐색하기

import sys

def get():
  return sys.stdin.readline().rstrip()


n = int(get())
arr = list(map(int, get().split()))
max_acc = int(get())

start, end = 1, max(arr)

while start <= end:
  mid = (start + end) // 2

  sum = 0

  for i in arr:
    if i <= mid:
      sum += i
    else:
      sum += mid

  if sum <= max_acc:
    start = mid + 1
  else:
    end = mid -1

print(end)