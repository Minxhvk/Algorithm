import sys

def get():
    return sys.stdin.readline().rstrip()

r, c = map(int, get().split())
arr = [list(map(str, get())) for _ in range(r)]
new_arr = [[] for _ in range(r)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

min_x = sys.maxsize
min_y = sys.maxsize
max_x = -1
max_y = -1

for i in range(r):
    for j in range(c):
        
        target_str = '.'
        sea_cnt = 0

        if arr[i][j] == 'X':
            for k in range(4):
                cur_dx = i + dx[k]
                cur_dy = j + dy[k]

                if cur_dx < 0 or cur_dx >= r or cur_dy < 0 or cur_dy >= c:
                    sea_cnt += 1
                    continue
                
                if arr[cur_dx][cur_dy] == '.':
                    sea_cnt += 1

            if sea_cnt >= 3:
                target_str = '.'
            else:
                target_str = 'X'

                min_x = min(min_x, i)
                max_x = max(max_x, i)
                min_y = min(min_y, j)
                max_y = max(max_y, j)

        new_arr[i].append(target_str)

for i in range(min_x, max_x+1):
    for j in range(min_y, max_y+1):
        print(new_arr[i][j], end='')
    print()
