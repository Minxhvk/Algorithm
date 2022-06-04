# 회의실 배정

import sys


def get():
    return sys.stdin.readline().rstrip()


N = int(get())
arr = []
total = 1

for i in range(N):
    arr.append(list(map(int, get().split())))

arr.sort(key=lambda x: (x[1], x[0]))
end_time = arr[0][1]

for i in range(1, N):
    if arr[i][0] >= end_time:
        end_time = arr[i][1]
        total += 1

print(total)
