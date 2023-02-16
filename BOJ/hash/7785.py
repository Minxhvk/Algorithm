import sys


def get():
    return sys.stdin.readline().rstrip()


n = int(get())
dict = dict()

for _ in range(n):
    name, status = get().split(' ')

    if status == 'enter':
        dict[name] = 1
    else:
        del dict[name]

for i in sorted(dict.keys(), reverse=True):
    print(i)
