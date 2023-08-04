import sys


def get():
    return sys.stdin.readline().rstrip()


n, m = map(int, get().split())

arr = list(map(int, get().split()))

pointer = 0
answer = sys.maxsize
tot = arr[0]

for i in range(n):
    while pointer < n and tot < m:
        pointer += 1
        if pointer < n:
            tot += arr[pointer]
    if pointer == n:
        break
    answer = min(answer, pointer-i+1)
    tot -= arr[i]

if answer == sys.maxsize:
    answer = 0

print(answer)
