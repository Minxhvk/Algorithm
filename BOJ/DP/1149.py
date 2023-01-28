import sys


def get():
    return sys.stdin.readline().rstrip()


n = int(get())
arr = []
result_arr = [[0 for _ in range(3)] for _ in range(n)]

for _ in range(n):
    arr.append(list(map(int, get().split())))

result_arr[0][0] = arr[0][0]
result_arr[0][1] = arr[0][1]
result_arr[0][2] = arr[0][2]

for i in range(1, n):
    result_arr[i][0] = min(result_arr[i-1][1], result_arr[i-1][2]) + arr[i][0]
    result_arr[i][1] = min(result_arr[i-1][0], result_arr[i-1][2]) + arr[i][1]
    result_arr[i][2] = min(result_arr[i-1][0], result_arr[i-1][1]) + arr[i][2]

print(min(result_arr[n-1][0], result_arr[n-1][1], result_arr[n-1][2]))
