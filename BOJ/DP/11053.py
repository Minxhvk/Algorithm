import sys


def get():
    return sys.stdin.readline().rstrip()


n = int(get())
input_arr = list(map(int, get().split()))

result_arr = [None for _ in range(n)]

result_arr[0] = 1

for i in range(1, n):
    result_max = -sys.maxsize
    for j in range(0, i):
        if input_arr[i] <= input_arr[j]:
            continue

        result_max = max(result_max, result_arr[j])

    if result_max == -sys.maxsize:
        result_arr[i] = 1
    else:
        result_arr[i] = result_max + 1

print(max(result_arr))
