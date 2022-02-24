

# 18258
from collections import deque
import sys

a = deque()
c = int(sys.stdin.readline())

for i in range(c):
    b = sys.stdin.readline().split()

    if b[0] == 'push':
        a.append(int(b[1]))

    elif b[0] == 'pop':
        print(a.popleft() if a else "-1")

    elif b[0] == 'size':
        print(len(a))

    elif b[0] == 'empty':
        print(0 if a else 1)

    elif b[0] == 'front':
        print(a[0] if a else "-1")

    elif b[0] == 'back':
        print(a[-1] if a else "-1")
