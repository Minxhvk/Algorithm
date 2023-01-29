import sys


def get():
    return sys.stdin.readline().rstrip().split()


# 첫 번째 풀이 시간초과
# n, m = map(int, get())
# arr = list(map(int, get()))
# arr_range = []
# answer = []

# for _ in range(m):
#     arr_range.append(list(map(int, get())))

# for i in arr_range:
#     answer.append(sum(arr[i[0]-1:i[1]]))

# for i in answer:
#     print(i)

# 두 번째 풀이 DP
n, m = map(int, get())
arr = list(map(int, get()))
arr_range = []
d = [0 for _ in range(n+1)]

for _ in range(m):
    arr_range.append(list(map(int, get())))

for i in range(1, n+1):
    d[i] = d[i-1] + arr[i-1]

for i in arr_range:
    print(d[i[1]] - d[i[0]-1])
