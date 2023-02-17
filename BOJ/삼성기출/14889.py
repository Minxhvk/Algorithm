import sys
import copy


def get():
    return sys.stdin.readline().rstrip()


N = int(get())

board = [list(map(int, get().split())) for _ in range(N)]
result = sys.maxsize
is_used = [False for _ in range(N+1)]


def divide_team(arr, idx):
    temp = copy.deepcopy(arr)

    if len(temp) == int(N/2):

        update_result(temp)

        is_used[idx] = False
        return

    for i in range(idx, N+1):
        if is_used[i] == True:
            continue

        is_used[i] = True
        temp.append(i)

        divide_team(temp, i)

        temp.pop()
        is_used[i] = False


def update_result(arr):

    extra_arr = [i for i in range(1, N+1) if i not in arr]

    global result
    result = min(result, abs(cal_score(arr) - cal_score(extra_arr)))


def cal_score(arr):
    temp_result = 0

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):

            x = arr[i] - 1  # is_used 등 0-index
            y = arr[j] - 1  # is_used 등 0-index

            temp_result += board[x][y] + board[y][x]

    return temp_result


if __name__ == "__main__":
    divide_team([], 1)

    print(result)
