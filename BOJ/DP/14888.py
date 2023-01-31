import sys


def get(): return sys.stdin.readline().rstrip()


n = int(get())

arr = list(map(int, get().split()))
operation = list(map(int, get().split()))  # 연산자 입력

result = []


def func(k, val, operation):
    if k == n-1:
        result.append(val)
        return

    for i in range(4):

        if operation[i] == 0:
            continue

        operation[i] -= 1
        temp = arr[k+1]

        if i == 0:
            func(k+1, val + temp, operation)
        elif i == 1:
            func(k+1, val - temp, operation)
        elif i == 2:
            func(k+1, val * temp, operation)
        else:
            func(k+1, int(val / temp), operation)
        operation[i] += 1


func(0, arr[0], operation)
print(max(result))
print(min(result))
