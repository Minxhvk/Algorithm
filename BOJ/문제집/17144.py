import sys

def get():
    return sys.stdin.readline().rstrip()

def diffusion():

    for i in range(R):
        for j in range(C):
            cur_num = board[i][j]

            if cur_num <= 0: continue

            cnt = 0
            d_num = int(cur_num/5)

            if d_num <= 0: continue

            for r in range(4):
                x = i + dx[r]
                y = j + dy[r]

                if x < 0 or x >= R or y < 0 or y >= C: 
                    continue
                
                if board[x][y] == -1:
                    continue

                add_list[x][y] += d_num
                cnt += 1

            add_list[i][j] -= d_num * cnt

    # 동시에 일어나므로, 이렇게 한 번에 처리해야 함.
    for i in range(R):
        for j in range(C):
            board[i][j] += add_list[i][j]
            add_list[i][j] = 0

def clean():

    # 위
    x = fresher[0]

    board[x-1][0] = 0
    for i in range(x-1, 0, -1):
        board[i][0] = board[i-1][0]
        board[i-1][0] = 0
    
    for i in range(C-1):
        board[0][i] = board[0][i+1]
        board[0][i+1] = 0

    for i in range(x):
        board[i][C-1] = board[i+1][C-1]
        board[i+1][C-1] = 0
    
    for i in range(C-1, 1, -1):
        board[x][i] = board[x][i-1]
        board[x][i-1] = 0

    # 아래
    x = fresher[1]
    board[x+1][0] = 0
    for i in range(x+1, R-1):
        board[i][0] = board[i+1][0]
        board[i+1][0] = 0

    for i in range(C-1):
        board[R-1][i] = board[R-1][i+1]
        board[R-1][i+1] = 0
    
    for i in range(R-1, x, -1):
        board[i][C-1] = board[i-1][C-1]
        board[i-1][C-1] = 0
    
    for i in range(C-1, 1, -1):
        board[x][i] = board[x][i-1]
        board[x][i-1] = 0
    

R, C, T = map(int, get().split())

board = []
add_list = [[0 for _ in range(C)] for _ in range(R)]
fresher = []

for i in range(R):
    temp_input = list(map(int, get().split()))
    if -1 in temp_input:
        fresher.append(i)

    board.append(temp_input)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


while T:
    diffusion()
    clean()

    T -= 1

answer = 0

for i in board:
    for j in i:
        if j > 0:
            answer += j

print(answer)