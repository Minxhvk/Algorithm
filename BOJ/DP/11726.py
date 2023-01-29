import sys


def get():
    return sys.stdin.readline().rstrip()


n = int(get())

arr = [0 for _ in range(n+1)]


if n == 1:
    print(1)
    exit()
elif n == 2:
    print(2)
    exit()

arr[1] = 1
arr[2] = 2

for i in range(3, n+1):
    arr[i] = (arr[i-1] + arr[i-2]) % 10007

print(arr[n])
