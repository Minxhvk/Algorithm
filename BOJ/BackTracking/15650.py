import sys


def get():
    return sys.stdin.readline().rstrip().split()


limit, size = map(int, get())
arr_value = [str(i) for i in range(1, limit+1)]
isused = [False for _ in range(limit)]


def func(k, arr):
    if len(arr) == size:
        print(' '.join(arr))
        return

    for i in range(k, limit):

        if isused[i] == True:
            continue

        isused[i] = True
        arr.append(arr_value[i])

        func(i+1, arr)

        arr.pop()
        isused[i] = False


func(0, [])
