def solution(board, moves):
    board_length = len(board)
    new_board = [[]]
    while board:
        for i in range(board_length):
            new_board[i].append(board[i].pop(0))
    return new_board


solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1],
         [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], 0)
