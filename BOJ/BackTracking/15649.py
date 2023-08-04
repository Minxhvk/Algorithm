import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

arr = [None for _ in range(m)]
isused = [False for _ in range(n + 1)]


def nNm(k):
    if k == m:
        print(' '.join(str(x) for x in arr))
        return

    for i in range(1, n+1):
        if isused[i] is False:
            arr[k] = i
            isused[i] = True
            nNm(k+1)
            isused[i] = False


nNm(0)
