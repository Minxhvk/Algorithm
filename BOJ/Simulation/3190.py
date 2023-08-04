import sys
from collections import deque


def get():
    return sys.stdin.readline().rstrip()


if __name__ == "__main__":

    answer = 0

    board_size = int(get())
    apple_cnt = int(get())

    board = [[0 for _ in range(board_size)] for _ in range(board_size)]
    move_arr = deque()
    snake_arr = deque([[0, 0]])

    for _ in range(apple_cnt):
        x, y = map(int, get().split())
        board[x-1][y-1] = 1

    move_cnt = int(get())

    for _ in range(move_cnt):
        sec, dircetion = get().split()
        move_arr.append([int(sec), str(dircetion)])

    forward = 0
    cur_x = 0
    cur_y = 0

    while True:

        answer += 1

        # 방향에 따른 좌표 변경
        if forward == 0: cur_y += 1
        elif forward == 1: cur_x += 1
        elif forward == 2: cur_y -= 1
        elif forward == 3: cur_x -= 1

        # 벽에 부딪혔을 경우
        if cur_x < 0 or cur_x >= board_size or cur_y < 0 or cur_y >= board_size: break

        # 몸에 부딪혔을 경우
        if [cur_x, cur_y] in snake_arr: break

        # 이동 좌표 추가
        snake_arr.append([cur_x, cur_y])

        # 사과 없음
        if board[cur_x][cur_y] == 0: snake_arr.popleft()
        # 사과 있음
        else: board[cur_x][cur_y] = 0

        # 방향 전환
        if move_arr:
            if answer == move_arr[0][0]:
                if move_arr[0][1] == "L":
                    if forward == 0: forward = 3
                    else: forward -= 1
                else:
                    if forward == 3: forward = 0
                    else: forward += 1

                move_arr.popleft()

    print(answer)



