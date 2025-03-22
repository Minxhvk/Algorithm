import sys

def get():
    return sys.stdin.readline().rstrip()

n = int(get())
arr = [list(map(int, get().split())) for _ in range(n)]
print(arr)