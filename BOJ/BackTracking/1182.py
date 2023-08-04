from itertools import combinations
import sys

# 백트래킹 풀이


def get():
    return sys.stdin.readline().rstrip().split()


def get_sum(idx, tot):
    global result

    if idx == size:
        if tot == target:
            result += 1

        return

    get_sum(idx+1, tot)  # 원소를 안 더한 상태로 진행
    get_sum(idx+1, tot + arr[idx])  # 원소를 더한 상태로 진행


if __name__ == "__main__":
    size, target = map(int, get())
    arr = list(map(int, get()))

    result = 0

    get_sum(0, 0)

    print(result)


# combinations 풀이 -> 이게 더 느림

size, target = map(int, get())
arr = list(map(int, get()))
result = 0
arr_2 = []

for i in range(size+1):
    arr_2 = list(combinations(arr, i))
    for j in arr_2:
        if len(j) < 1:
            continue
        if sum(j) == target:
            result += 1

print(result)
