# 꿀 따기
import sys


def get():
    return sys.stdin.readline().rstrip()


N = int(get())
arr = list(map(int, get().split()))
prefix_sum = []
prefix_sum.append(arr[0])
ans = 0

# 누적합 계산
for i in range(1, N):
    prefix_sum.append(prefix_sum[i - 1] + arr[i])

# 벌 - 벌 - 꿀
for i in range(1, N-1):
    ans = max(ans, prefix_sum[N-1] - arr[0] +
              prefix_sum[N-1] - prefix_sum[i] - arr[i])

# 꿀 - 벌 - 벌
for i in range(1, N-1):
    ans = max(ans, prefix_sum[N-2] + prefix_sum[i-1] - arr[i])

# 벌 - 꿀 - 벌
for i in range(1, N-1):
    ans = max(ans, prefix_sum[N-2] - arr[0] + arr[i])

print(ans)
