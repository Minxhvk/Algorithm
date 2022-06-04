# 에너지 드링크

import sys


def get():
    return sys.stdin.readline().rstrip()


N = get()
arr = list(map(int, get().split()))

arr.sort()

for i in range(len(arr) - 1):
    arr[-1] += arr[i] / 2

print(arr[-1])
