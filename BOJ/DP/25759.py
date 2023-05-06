# 실패 -> 다시

import sys

def get():
    return sys.stdin.readline().rstrip()


N = int(get())

arr = list(map(int, get().split()))
answer = [0 for _ in range(N)]

for i in range(1, N):
    answer[i] = max(answer[i-1] + abs(arr[i]-arr[i-1])**2, abs(arr[i]-arr[0])**2)

print(answer[N-1])
