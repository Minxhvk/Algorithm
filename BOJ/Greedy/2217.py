import sys


def get():
    return sys.stdin.readline().rstrip()


n = int(get())
arr = []

for _ in range(n):
    arr.append(int(get()))

LENGTH = len(arr)

arr = sorted(arr, reverse=False)

result = 0

for i in range(LENGTH):
    result = max(result, arr[i] * (LENGTH - i))

print(result)
