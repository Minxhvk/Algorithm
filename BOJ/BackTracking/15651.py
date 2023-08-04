import sys


def get():
    return sys.stdin.readline().rstrip().split()


limit, size = map(int, get())


def func(k, arr):
    if k == size:
        print(' '.join(arr))
        return

    for i in range(1, limit + 1):

        arr.append(str(i))

        func(k+1, arr)

        arr.pop()


func(0, [])
