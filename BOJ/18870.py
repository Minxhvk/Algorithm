import sys

def get():
    return sys.stdin.readline().rstrip()

n = int(get())
arr = list(map(int, get().split()))

sotted_arr = sorted(list(set(arr)))

dict = {sotted_arr[i]:i for i in range(len(sotted_arr))}

for i in arr:
  print(dict[i], end=" ")

