import sys

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
is_used = [ 0 for _ in range(10)]
choose = [0 for _ in range(10)]

def dfs(idx, cnt):
    global n, m
    
    if cnt == m:
        for i in range(cnt):
            print(arr[choose[i]], end=" ")
        print()
    
    for i in range(idx, n):
        if is_used[i]:
            continue
        choose[cnt] = i

        is_used[i] = 1
        dfs(i+1, cnt+1)
        is_used[i] = 0

dfs(0, 0)
