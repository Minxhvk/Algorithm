import sys
from collections import deque

start, target = map(int, sys.stdin.readline().rstrip().split())

visited = [False for _ in range(100001)]

q = deque([[start, 0]])

while True:
    q_pop = q.popleft()
    cur_x = q_pop[0]
    cur_time = q_pop[1]

    # Already Visited
    visited[cur_x] = True

    if cur_x == target:
        print(cur_time)
        break

    if cur_x * 2 < 100001 and not visited[cur_x * 2]:
        q.append([cur_x * 2, cur_time])

    if cur_x - 1 > -1 and not visited[cur_x - 1]:
        
        q.append([ cur_x - 1, cur_time + 1 ])
    
    if cur_x + 1 < 100001 and not visited[cur_x + 1] :
        q.append([cur_x + 1, cur_time + 1])
      
    
    
    