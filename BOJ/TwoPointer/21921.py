import sys

def get():
  return sys.stdin.readline().rstrip()

N, X = map(int, get().split())

arr = list(map(int, get().split()))

cnt = 1
cur_num = sum(arr[:X])
answer = cur_num

for i in range(N):
  target = i + X

  if target >= N:
    continue

  cur_num = cur_num - arr[i] + arr[target]

  if cur_num > answer:
    cnt = 1
    answer = cur_num
  elif cur_num == answer:
    cnt += 1

if answer == 0:
  print("SAD")
else:
  print(answer)
  print(cnt)