# 동전 0

import sys


def get():
    return sys.stdin.readline().rstrip()


N, total = map(int, get().split())
coin = []
result = 0

for i in range(N):
    validation_num = int(get())
    if validation_num > total:
        continue
    else:
        coin.append(validation_num)

for i in coin[::-1]:
    result += total//i
    total = total % i

print(result)
