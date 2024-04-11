import sys
from collections import deque

def get():
    return sys.stdin.readline().rstrip()

class Shark:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.size = 2
        self.eat = 0

class Fish:
    def __init__(self, x, y, dist) -> None:
        self.x = x
        self.y = y
        self.dist = dist


N = int(get())
board = []
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

shark = Shark()
que = deque()
answer = 0

for i in range(N):
    temp = list(map(int, get().split()))

    for j in range(N):
        if temp[j] == 9:
            shark.x, shark.y = i, j
            temp[j] = 0

    board.append(temp)

while True:
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[shark.x][shark.y] = True

    fish_list = []

    que.append([shark.x, shark.y, 0])

    while que:
        que_x, que_y, que_dist = que.popleft()

        for i in range(4):
            x = que_x + dx[i]
            y = que_y + dy[i]

            if x < 0 or x >= N or y < 0 or y >= N: continue
            
            if visited[x][y]: continue

            if board[x][y] > shark.size: continue

            visited[x][y] = True

            if board[x][y] == shark.size or board[x][y] == 0:
                que.append([x, y, que_dist+1])
            else:
                fish_list.append(Fish(x, y, que_dist + 1))
    
    if fish_list:
        fish_list.sort(key=lambda fish: [fish.dist, fish.x, fish.y])

        fish = fish_list[0]

        shark.x = fish.x
        shark.y = fish.y
        shark.eat += 1

        answer += fish.dist

        board[shark.x][shark.y] = 0

        if shark.size == shark.eat:
            shark.size += 1
            shark.eat = 0

        que.clear()
        fish_list.clear()

    else:
        break
        
print(answer)
