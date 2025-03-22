import sys

def get():
    return sys.stdin.readline().rstrip()

n, m = map(int, get().split())
arr = sorted(list(map(int, get().split())))
choose = [ 0 for _ in range(10)]
is_used = [ 0 for _ in range(10)]

def dfs(cnt):

    if cnt == m:
        for i in range(cnt):
            print(arr[choose[i]], end=' ')
        print()
        return 0

    for i in range(0, n):
        choose[cnt] = i
        dfs(cnt+1)

dfs(0)