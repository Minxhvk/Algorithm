import sys

def get():
  return sys.stdin.readline().rstrip()

_ = int(get())

board = list(map(int, get().split()))
answer = 0

for i in board:
  if i == 1: continue

  temp_i = 2
  is_prime = True
  while temp_i * temp_i <= i:
    if i % temp_i == 0:
      is_prime = False
      break
    
    temp_i += 1

  if is_prime: answer += 1

print(answer)
  
