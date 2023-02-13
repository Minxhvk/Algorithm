import sys


def get():
    return sys.stdin.readline().rstrip()


n, m = map(int, get().split())
arr = []

for _ in range(n):
    arr.append(int(get()))

arr = sorted(arr)

# 내 풀이 200ms
p1 = 0
p2 = 0
min_size = sys.maxsize

while p1 < n-1:

    if arr[p2] - arr[p1] >= m:
        min_size = min(min_size, arr[p2] - arr[p1])
        p1 += 1

    else:
        if p2 == n-1:
            p1 += 1
        else:
            p2 += 1

print(min_size)


# 바킹독님 풀이 188ms
p2 = 0
min_size = sys.maxsize


for i in range(n):
    while (p2 < n and arr[p2] - arr[i] < m):
        p2 += 1
    if p2 == n:
        break
    min_size = min(min_size, arr[p2] - arr[i])


print(min_size)
