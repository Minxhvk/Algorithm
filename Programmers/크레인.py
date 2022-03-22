def solution(board, moves):
    answer = [None]
    cnt = 0
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] > 0:
                if answer[-1] == board[i][move-1]:
                    answer.pop()
                    cnt += 1
                else:
                    answer.append(board[i][move-1])
                board[i][move-1] = 0
    return cnt*2
