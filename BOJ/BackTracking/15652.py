import sys


n, m = map(int, sys.stdin.readline().rstrip().split())


def nNm(k, arr, cur):
    if k == m:
        print(' '.join(map(str, arr)))
        return

    for i in range(cur, n+1):
        arr.append(i)
        nNm(k+1, arr, i)
        arr.remove(i)


nNm(0, [], 1)
