import sys
from collections import deque

def get():
    return sys.stdin.readline().rstrip()

if __name__ == "__main__":
    dx = [-1, -2, -1, -2,  1,  2, 1, 2]
    dy = [-2, -1,  2,  1, -2, -1, 2, 1]

    N = int(get())

    for _ in range(N):
        que = deque()
        size = int(get())
        cur_x, cur_y = map(int, get().split())
        target_x, target_y = map(int, get().split())
        visited = [[0 for _ in range(size)] for _ in range(size)]

        que.append([cur_x, cur_y, 0])
        answer = None

        visited[cur_x][cur_y] = 1

        if cur_x == target_x and cur_y == target_y:
            print(0)
            continue

        while que and answer is None:
            cur_x, cur_y, cnt = que.popleft()

            for i in range(8):
                x = cur_x + dx[i]
                y = cur_y + dy[i]

                if x < 0 or x >= size or y < 0 or y >= size: continue
                if visited[x][y] == 1: continue

                if x == target_x and y == target_y:
                    answer = cnt + 1
                    break

                visited[x][y] = 1
                que.append([x, y, cnt + 1])

        print(answer if answer else 0)