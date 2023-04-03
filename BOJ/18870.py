import sys

def get():
    return sys.stdin.readline().rstrip()

n = int(get())
arr = list(map(int, get().split()))

sotted_arr = sorted(list(set(arr)))

for i in arr:
  print(sotted_arr.index(i), end=" ")

