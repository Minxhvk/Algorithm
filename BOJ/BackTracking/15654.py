import sys

def get():
    return sys.stdin.readline().rstrip()

n, m = map(int, get().split())
arr = sorted(list(map(int, get().split())))

choose = [ 0 for _ in range(10)]
used = [ 0 for _ in range(10)]

def dfs(cnt):
    global n, m

    if cnt == m:
        for idx in range(cnt):
            print(arr[choose[idx]], end=' ')
        print()
        return
    
    for i in range(0, n):
        if used[i]:
            continue
        used[i] = 1
        choose[cnt] = i
        dfs(cnt + 1)
        used[i] = 0
        
dfs(0)



