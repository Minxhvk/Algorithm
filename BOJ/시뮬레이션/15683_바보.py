import sys

# 틀린 풀이. 조합을 생각하지 않았음.


def get():
    return sys.stdin.readline().rstrip()


def row_right(col, row, m):
    temp_list = []
    for temp_row in range(row, m):
        if board[col][temp_row] == 6:
            break
        elif board[col][temp_row] != 0:
            continue

        temp_list.append([col, temp_row])

    return temp_list


def row_left(col, row):
    temp_list = []
    for temp_row in range(row, -1, -1):
        if board[col][temp_row] == 6:
            break
        elif board[col][temp_row] != 0:
            continue

        temp_list.append([col, temp_row])

    return temp_list


def col_up(col, row):
    temp_list = []
    for temp_col in range(col, -1, -1):
        if board[temp_col][row] == 6:
            break
        elif board[temp_col][row] != 0:
            continue

        temp_list.append([temp_col, row])

    return temp_list


def col_down(col, row, n):
    temp_list = []

    for temp_col in range(col, n):
        if board[temp_col][row] == 6:
            break
        elif board[temp_col][row] != 0:
            continue

        temp_list.append([temp_col, row])

    return temp_list


if __name__ == '__main__':
    n, m = map(int, get().split())

    board = []

    for _ in range(n):
        board.append(list(map(int, get().split())))

    all_case = []

    cnt = 0

    for col in range(n):
        for row in range(m):
            cur_office = board[col][row]

            if cur_office == 0:
                cnt += 1

            if cur_office == 1:

                # 왼쪽 방향
                counter_1_1 = row_left(col, row)

                # 오른쪽 방향
                counter_1_2 = row_right(col, row, m)

                # 아래 방향
                counter_1_3 = col_down(col, row, n)

                # 위 방향
                counter_1_4 = col_up(col, row)

                all_case.append(max(counter_1_1, counter_1_2,
                                counter_1_3, counter_1_4, key=len))

            elif cur_office == 2:
                # <->
                counter_2_1 = row_right(col, row, m) + row_left(col, row)

                # 세로
                counter_2_2 = col_down(col, row, n) + col_up(col, row)

                all_case.append(max(counter_2_1, counter_2_2, key=len))

            elif cur_office == 3:
                # ㄴ
                counter_3_1 = row_right(col, row, m) + col_up(col, row)

                # 오른쪽, 아래
                counter_3_4 = row_right(col, row, m) + col_down(col, row, n)

                # ㄱ
                counter_3_2 = row_left(col, row) + col_down(col, row, n)

                # 왼쪽, 위
                counter_3_3 = row_left(col, row) + col_up(col, row)

                all_case.append(max(counter_3_1, counter_3_2,
                                counter_3_3, counter_3_4, key=len))

            elif cur_office == 4:
                # ㅗ
                counter_4_1 = row_right(col, row, m) + \
                    row_left(col, row) + col_up(col, row)

                # ㅜ
                counter_4_2 = row_right(col, row, m) + \
                    row_left(col, row) + col_down(col, row, n)

                # ㅓ
                counter_4_3 = row_left(col, row) + \
                    col_up(col, row) + col_down(col, row, n)

                # ㅏ
                counter_4_4 = row_right(col, row, m) + \
                    col_up(col, row) + col_down(col, row, n)

                all_case.append(max(counter_4_1, counter_4_2, key=len))

            elif cur_office == 5:
                all_case.append(row_right(col, row, m) + row_left(col, row) +
                                col_up(col, row) + col_down(col, row, n))

    result = []
    for i in all_case:
        for j in i:
            if j in result:
                continue
            result.append(j)

    print(cnt - len(result))
