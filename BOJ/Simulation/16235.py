import sys

def get():
    return sys.stdin.readline().rstrip()

def spring(board, tree_list):
    die_tree_list = []

    for i in range(N):
        for j in range(N):

            # 정렬 여기서 한 번만 해도 됨
            tree_list[i][j] = sorted(tree_list[i][j])
            
            # 더 좋은 선택지
            # for i in range(n):
            #     for j in range(n):
            #         len_ = len(trees[i][j])  # 현재 위치에 있는 나무 총 개수
            #         # 현재 위치의 나무들 탐색
            #         for k in range(len_):
            #             # 나무가 죽는 경우
            #             if graph[i][j] < trees[i][j][k]:
            #                 # 죽는 나무들은 따로 저장
            #                 for _ in range(k, len_):
            #                     dead_trees[i][j].append(trees[i][j].pop())
            #                 break
            #             # 나무가 양분 먹고 성장하는 경우
            #             else:
            #                 graph[i][j] -= trees[i][j][k]
            #                 trees[i][j][k] += 1
            
            del_count = 0
            for idx, temp_tree in enumerate(tree_list[i][j][:]):
                if board[i][j] < temp_tree:
                    die_tree_list.append([i, j, temp_tree])
                    del tree_list[i][j][idx-del_count]
                    del_count += 1
                else:
                    board[i][j] -= temp_tree
                    tree_list[i][j][idx-del_count] += 1

    return die_tree_list


def summer(board, die_tree_list):

    for tree in die_tree_list:
        x = tree[0]
        y = tree[1]
        age = int(tree[2] / 2)

        board[x][y] += age

def fall(tree_list):
    for i in range(N):
        for j in range(N):
            # TODO : Time Out
            for tree in tree_list[i][j]:
                if tree % 5 == 0:
                    if i-1 >= 0: tree_list[i-1][j].append(1)
                    if j-1 >= 0: tree_list[i][j-1].append(1)
                    if i-1 >= 0 and j-1 >=0: tree_list[i-1][j-1].append(1)
                    if i+1 < N: tree_list[i+1][j].append(1)
                    if j+1 < N: tree_list[i][j+1].append(1)
                    if i+1 < N and j+1 < N: tree_list[i+1][j+1].append(1)
                    if i+1 < N and j-1 >= 0: tree_list[i+1][j-1].append(1)
                    if i-1 >= 0 and j+1 < N: tree_list[i-1][j+1].append(1)

def winter(board, S2D2):
    for i in range(N):
        for j in range(N):
            board[i][j] += S2D2[i][j]


if __name__ == "__main__":

    N, M, K = map(int, get().split())
    
    board = [[5 for _ in range(N)] for _ in range(N)]
    
    S2D2 = [list(map(int, get().split(' '))) for _ in range(N)]

    tree_list = [[[] for _ in range(N)] for _ in range(N)]

    for _ in range(M):
        x, y, age = list(map(int, get().split()))
        tree_list[x-1][y-1].append(age)
            
        tree_list[x-1][y-1] = sorted(tree_list[x-1][y-1])


    for _ in range(K):
        summer(board, spring(board, tree_list))
        fall(tree_list)
        winter(board, S2D2)

    answer = 0

    for i in range(N):
        for j in range(N):
            answer += len(tree_list[i][j])
    print(answer)