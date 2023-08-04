import sys


def get():
    return sys.stdin.readline().rstrip().split()


n, m, c = map(int, get())

board = [[0 for _ in range(m)] for _ in range(n)]
st_list = [[] for _ in range(c)]

for i in range(c):
    temp_n, temp_m = map(int, get())

    for _ in range(temp_n):
        st_list[i].append(list(map(int, get())))

print(st_list)
