import sys
from collections import deque

def get():
    return sys.stdin.readline().rstrip()

n = int(get())
node_cnt = int(get())
net = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(node_cnt):
    a, b = map(int, get().split())
    net[a].append(b)
    net[b].append(a)

q = deque()
count = 0
q.append(1)
visited[1] = True

while q:
    cur = q.popleft()
    for val in net[cur]:
        if not visited[val]:
            q.append(val)
            visited[val] = True
            count += 1
print(count)