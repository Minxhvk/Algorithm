import sys

def get():
  return sys.stdin.readline().rstrip()

N = int(input())

div_num = 2

while div_num * div_num <= N:

  while (N % div_num == 0):
    print(div_num)
    N /= div_num
  
  
  div_num += 1 

if N != 1:
   print(int(N))
  