import sys

def get():
  return sys.stdin.readline().rstrip()

# 최대 공약수
def gcd(a, b):
  if (a == 0): return b
  return gcd(b%a, a)

# 최소 공배수
def lcm(a, b):
  return int(a / gcd(a, b)) * b

def solve(m, n, x, y):
  if x == m: x= 0
  if y == n: y = 0
  l = lcm(m, n)
  for i in range(x, l+1, m):
    if i == 0: continue
    if i % n == y: return i
    
  return -1

T = int(get())

board = [list(map(int, get().split())) for _ in range(T)]

for M, N, x, y in board:
  print(solve(M, N, x, y))
