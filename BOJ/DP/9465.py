# 첫 번째 풀이 -> 시간 초과.

import sys
# from heapq import heappop, heappush

def get():
    return sys.stdin.readline().rstrip()

# def get_max_score(heap, board, temp_n):
    
#     rtn = 0

#     while heap:
#         target = -heappop(heap)

#         for i in range(2):
#             for j in range(temp_n):
                
#                 if board[i][j] != target: continue

                
#                 # 동일한 요소 찾음
#                 board[i][j] = -1
#                 rtn += target

#                 for k in range(4):
#                     x = i + dx[k]
#                     y = j + dy[k]
                    
#                     # idx 검사
#                     if x < 0 or y < 0 or x >= 2 or y >= temp_n: continue
                    
#                     board[x][y] = -1
#     return rtn
                    


# N = int(get())
# answer = []
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# for _ in range(N):
#     board = []
#     heap = []

#     temp_n = int(get())
    
#     for _ in range(2):
#         temp_list = list(map(int, get().split()))
#         board.append(temp_list)
#         for i in temp_list:
#             heappush(heap, -i)

#     answer.append(get_max_score(heap, board, temp_n))
        
    
    
# for i in answer:
#     print(i)


# 두번째 풀이 : DP 
# 2개 행으로, 각 행마다 N열의 최댓값을 DP에 저장한다.
# 0행의 스티커를 뜯음 -> 다음은 대각선 스티커를 뜯을 수 밖에 없으므로 +
# 다음 대각선을 뜯는 것이 아닌, 다다음 대각선을 뜯었을 경우 최댓값이 나올 수 있다.
N = int(get())
answer = []

for _ in range(N):
    T = int(get())

    board = [list(map(int, get().split())) for _ in range(2)]

    dp = [[0 for _ in range(T)] for _ in range(2)]

    if T == 1:
        answer.append(max(board[0][0], board[1][0]))
    elif T == 2:
        answer.append(max(board[1][0] + board[0][1], board[0][0] + board[1][1]))
    else:
        dp[0][0], dp[1][0] = board[0][0], board[1][0]

        dp[0][1] = board[1][0] + board[0][1]
        dp[1][1] = board[0][0] + board[1][1]

        for i in range(2, T):
            # i-1번째 최댓값을 선택하지 않을 경우에 최대가 될 수 있음.
            dp[0][i] = max(dp[1][i-1], dp[0][i-2], dp[1][i-2]) + board[0][i]
            dp[1][i] = max(dp[0][i-1], dp[1][i-2], dp[0][i-2]) + board[1][i]

        answer.append(max(dp[0][T-1], dp[1][T-1]))

for i in answer:
    print(i)