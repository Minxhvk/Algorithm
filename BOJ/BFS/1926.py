import sys


def get():
    return sys.stdin.readline().rstrip()


x, y = map(int, get().split())

board = []  # 좌표 저장
vis = [[0 for _ in range(y)] for _ in range(x)]  # 방문 저장
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
cnt = 0  # 그림 수
width = 0  # 넓이

cur = []

for _ in range(x):
    board.append(list(map(int, get().split())))

for i in range(x):
    for j in range(y):
        if board[i][j] == 0 or vis[i][j]:
            continue  # 방문 했거나, 색칠 안되어 있을 경우

        cnt += 1  # 그림 수 ++
        q = []  # 값 넣을 큐

        vis[i][j] = 1
        q.append([i, j])  # 큐에 좌표 삽입

        area = 0

        while len(q) > 0:
            cur = q.pop(0)
            area += 1
            for idx in range(4):
                nx = cur[0] + dx[idx]
                ny = cur[1] + dy[idx]
                if nx < 0 or ny < 0 or nx >= x or ny >= y:
                    continue
                if board[nx][ny] == 0 or vis[nx][ny]:
                    continue
                vis[nx][ny] = 1
                q.append([nx, ny])
        width = max(width, area)

print(cnt)
print(width)
