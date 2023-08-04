import sys
from collections import deque

def get():
    return sys.stdin.readline().rstrip()

N = int(get())

board = [list(map(int, get())) for _ in range(N)]
dist = [[0 for _ in range(N)] for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

que = deque()

all_cnt = 0
per_cnt_list = []


for x in range(N):
    for y in range(N):
        
        if board[x][y] == 0 or dist[x][y] == 1: continue
        
        que.append([x, y])
        dist[x][y] = 1
        
        all_cnt += 1
        per_cnt = 0
        while len(que) > 0:
            cur = que.popleft()
            per_cnt += 1 # Per Cnt ++

            for idx in range(4):
                cur_x = cur[0] + dx[idx]
                cur_y = cur[1] + dy[idx]

                # Index Out Of Range
                if cur_x < 0 or cur_x >= N or cur_y < 0 or cur_y >=  N : continue 
                # Visited
                if dist[cur_x][cur_y] == 1 : continue
                # Not Home
                if board[cur_x][cur_y] == 0 : continue 

                que.append([cur_x, cur_y]) # ADD
                dist[cur_x][cur_y] = 1 # Visit Check

        per_cnt_list.append(per_cnt)

per_cnt_list = sorted(per_cnt_list)

print(all_cnt)
for i in per_cnt_list:
    print(i)

                    
            
