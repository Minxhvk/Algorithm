def solution(board, moves):
    bucket = [None]
    cnt = 0
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] > 0:
                if bucket[-1] == board[i][move-1]:
                    bucket.pop()
                    cnt += 1
                else:
                    bucket.append(board[i][move-1])
                board[i][move-1] = 0
                break

    return (cnt * 2)