import sys

def get():
    return sys.stdin.readline().rstrip()

n, l = map(int, get().split())

board = [list(map(int, get().split())) for _ in range(n)]

answer = 0

def is_pass(arr):
    
    is_used = [False for _ in range(n)]

    for i in range(n-1):
        
        cur = arr[i]
        next = arr[i+1]

        # 차이가 1 이상
        if abs(cur - next) > 1: return False
        
        if cur + 1 == next : # 2 2 2 3   2 3
            if i - l + 1 < 0: # index check
                return False
            for k in range(i, i-l, -1):
                if is_used[k]: return False

                if arr[k] == cur: is_used[k] = True
                else: return False
          
        if cur - 1 == next : # 3 2 2 2  i == 0  1 ~ 2
            if i + l >= n: # index check
                return False
            
            for k in range(i+1, i+l+1):
                if is_used[k]: return False

                if arr[k] == next: is_used[k] = True
                else: return False

    return True
                  
# 행
for row in board:

    if is_pass(row):
        answer += 1

# 열
for i in range(n):
    arr = []
    for j in range(n):
        arr.append(board[j][i])
    
    if is_pass(arr):
        answer+=1
        
print(answer)