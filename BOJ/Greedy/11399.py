# ATM
# 제일 첫번째 숫자는 size 만큼 곱해지고 그 다음은 숫자는 size - 1 만큼 곱해진다.
# 따라서 정렬한 후 작은 수 부터 실행하면 최적합을 찾을 수 있다.
import sys


def get():
    return sys.stdin.readline()


size = int(get())
arr = list(map(int, get().split()))
arr.sort()
result = 0

for i in arr:
    result += (i * size)
    size -= 1


print(result)
