import sys

def get():
  return sys.stdin.readline().rstrip()


N = int(get())

if N % 2 == 0:
  print("CY")
else:
  print("SK")