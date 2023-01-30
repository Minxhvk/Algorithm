import sys


def get(): return sys.stdin.readline().rstrip()


n = int(get())

arr = list(map(int, get().split()))
d = list(map(int, get().split()))  # 연산자 입력
up_d = []  # 연산자 치환
is_used = [False for _ in range(n-1)]

for i in range(4):
    if d[i] == 0:
        continue
    if i == 0:
        for _ in range(d[i]):
            up_d.append('+')
    elif i == 1:
        for _ in range(d[i]):
            up_d.append('-')
    elif i == 2:
        for _ in range(d[i]):
            up_d.append('*')
    else:
        for _ in range(d[i]):
            up_d.append('/')

result = []


def func(k, val):
    if k == n-1:
        result.append(val)
        return

    for i in range(n-1):
        if is_used[i] == True:
            continue

        is_used[i] = True
        temp = arr[k+1]

        if up_d[i] == '+':
            func(k+1, val + temp)
        elif up_d[i] == '-':
            func(k+1, val - temp)
        elif up_d[i] == '*':
            func(k+1, val * temp)
        else:
            func(k+1, int(val / temp))

        is_used[i] = False


func(0, arr[0])
print(max(result))
print(min(result))
