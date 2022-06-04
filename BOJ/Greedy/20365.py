# 블로그 2

import sys


def get():
    return sys.stdin.readline().rstrip()


N = int(get())
arr = str(get())
blue = 0
red = 0

if arr[0] == 'R':
    red += 1
else:
    blue += 1

for i in range(1, N):
    if arr[i] != arr[i-1]:
        if arr[i] == 'R':
            red += 1
        else:
            blue += 1

print(min(red, blue) + 1)
