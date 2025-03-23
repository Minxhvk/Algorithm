import sys

def get():
    return sys.stdin.readline().rstrip()

n, m = map(int, get().split())

arr = sorted(list(map(int, get().split())))
choose = [0 for _ in range(10)]
used = [0 for _ in range(10)]

def nNm(idx):
    global n, m

    if idx == m:
        for i in range(idx):
            print(arr[choose[i]], end=" ")
        print()
        return 0

    pre = -1
    for i in range(n):
        if used[i] or pre == arr[i]: continue
        
        pre = arr[i]
        choose[idx] = i

        used[i] = 1
        nNm(idx+1)
        used[i] = 0

nNm(0)