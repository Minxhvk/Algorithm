import sys
from collections import deque

def get():
    return sys.stdin.readline().rstrip()

n = int(get())
vertices = [[0] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, get().split())
    vertices[a].append(b)
    vertices[b].append(a)

parent = [0]*(n+1)	# 각 노드들의 부모를 기록하는 배열

q = deque()
q.append(1)

while q:
    cur = q.popleft()
    for v in vertices[cur]:
        # 이미 parent에 기록되었다는 것은 부모가 있다는 뜻
        # 이 정점과 연결된 것들은 자식이 됨
        if parent[v] == 0:	
            parent[v] = cur
            q.append(v)

for p in parent[2:]:
	print(p)