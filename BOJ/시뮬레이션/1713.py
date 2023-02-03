import sys


def get():
    return sys.stdin.readline().rstrip()


n = int(get())
m = int(get())

arr = list(map(int, get().split(' ')))

board = [[None, None, None] for _ in range(n)]
continue_flag = False
time_cnt = 0

for i in range(m):

    # 이미 존재하는지 확인
    for j in range(n):
        if board[j][0] == arr[i]:
            board[j][1] += 1
            continue_flag = True
            break

    if continue_flag:
        continue_flag = False
        continue

    # 빈 칸 확인
    for j in range(n):
        if board[j][0] is None:
            board[j][0] = arr[i]
            board[j][1] = 0
            time_cnt += 1
            board[j][2] = time_cnt
            continue_flag = True
            break

    if continue_flag:
        continue_flag = False
        continue

    # 꽉 찼다면
    temp_min = [None, sys.maxsize, None]
    for j in range(n):
        if board[j][1] < temp_min[1]:
            temp_min = [j, board[j][1], board[j][2]]

        if board[j][1] == temp_min[1]:
            if board[j][2] < temp_min[2]:
                temp_min = [j, board[j][1], board[j][2]]

    board[temp_min[0]][0] = arr[i]
    board[temp_min[0]][1] = 0
    time_cnt += 1
    board[temp_min[0]][2] = time_cnt

result = []
for i in board:
    if i[0] is None:
        continue

    result.append(i[0])

result = sorted(result)

print(' '.join(map(str, result)))
