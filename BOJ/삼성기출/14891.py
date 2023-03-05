import sys

def get():
    return sys.stdin.readline().rstrip()

def rotation(arr):
    for i in range(4):
        
        direction = arr[i]
        target = board[i]

        if direction == None: continue

        elif direction == -1:
            # deque
            target.append(target.pop(0))
        else:
            target.insert(0, target.pop())

        board[i] = target
        

board = [list(map(int, get())) for _ in range(4)]
n = int(get())
target = [list(map(int, get().split())) for _ in range(n)]


for i in range(n):
    
    is_change = [None for _ in range(4)]

    num = target[i][0] -1

    is_change[num] = target[i][1]
 
    # 왼쪽 보기
    if num-1 >= 0:
      for k in range(num-1, -1, -1):
          if is_change[k+1] == None: break

          # 같을 경우 회전 X -> 앞으로도 안하므로 안봐도 됨
          if board[k+1][6] == board[k][2] : break
          else:
              if is_change[k+1] == -1:
                  is_change[k] = 1
              else:
                  is_change[k] = -1

    if num+1 < 4:
        for k in range(num+1, 4):
            if is_change[k-1] == None: break

            # 같을 경우 회전 X -> 앞으로도 안하므로 안봐도 됨
            if board[k-1][2] == board[k][6] : break
            else:
                if is_change[k-1] == -1:
                  is_change[k] = 1
                else:
                  is_change[k] = -1

    rotation(is_change)


answer = 0
for i in range(4):
   if board[i][0] == 1:
      answer += 2**i

print(answer)
                
            

              





             





