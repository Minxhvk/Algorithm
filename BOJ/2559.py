import sys

def get():
    return sys.stdin.readline().rstrip()

n, k = map(int, get().split())

arr = list(map(int, get().split()))

answer = sum(arr[:k])
pre_sum = sum(arr[:k])
cur_idx = 0

for i in range(k, len(arr)):
    cur_sum = pre_sum - arr[cur_idx] + arr[i]
    cur_idx += 1

    answer = max(answer, cur_sum)
    pre_sum = cur_sum

print(answer)

    