import sys

def get ():
  return sys.stdin.readline().rstrip()

N, K, Q, M = map(int, get().split())

sleep = [0 for _ in range(N+3)]
check = [0 for _ in range(N+3)]

k_arr = list(map(int, get().split()))
q_arr = list(map(int, get().split()))

for i in k_arr: sleep[i] = 1

for i in q_arr:
  if sleep[i]: continue

  for j in range(i, N+3, i):
    if sleep[j]: continue
    check[j] = 1

p_sum = [0 for _ in range(N+3)]
for i in range(3, N+3):
  p_sum[i] = p_sum[i-1] + check[i]

for _ in range(M):
  s, e = map(int, get().split())
  print(e - s + 1 - (p_sum[e] - p_sum[s-1]))




