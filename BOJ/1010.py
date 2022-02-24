
# 1010

import math

t = int(input())
a = [[0 for col in range(2)] for row in range(t)]

for i in range(t):
    a[i][0], a[i][1] = map(int, input().split())

for i in range(t):
       print(int(math.factorial(a[i][1]) / (math.factorial(a[i][1]-a[i][0]) * math.factorial(a[i][0]))))