import sys
from collections import deque

def get():
    return sys.stdin.readline().rstrip()

n = int(get())

arr = [[] for _ in range(n+1)]
parent = [0 for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, get().split())
    arr[a].append(b)
    arr[b].append(a)

q = deque()
q.append(1)
parent[1] = 1

while q:
    cur = q.popleft()

    for i in arr[cur]:
        if parent[i] == 0:
            parent[i] = cur
            q.append(i)

for i in parent[2:]:
    print(i)