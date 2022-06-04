# 서강근육맨
import sys


def get():
    return sys.stdin.readline().rstrip()


N = get()
arr = list(map(int, get().split()))

arr.sort()
result = 0

if(len(arr) % 2 == 0):
    for i in range(int(len(arr) / 2)):
        result = max(result, arr[i] + arr[(-i - 1)])
else:
    result = arr[-1]
    for i in range(int(len(arr) / 2)):
        result = max(result, arr[i] + arr[len(arr) - i - 2])

print(result)
