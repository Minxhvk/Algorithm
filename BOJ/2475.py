import sys

a = []
a = list(map(int, sys.stdin.readline().split()))
i = 0
for j in a:
    i += (j ** 2)

print(int(i) % 10)
