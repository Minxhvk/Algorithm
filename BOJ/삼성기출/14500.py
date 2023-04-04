import sys

def get():
    return sys.stdin.readline().rstrip()


n, m = map(int, get().split())

board = [list(map(int, get().split())) for _ in range(n)]

terlomino = [[0, 0, 0, 0]]
terlomino = [[0], [0], [0, 0]]

terlomino = [[0, 0], [0, 0]]
terlomino = [[0, 0, 0, 0]]