import math

def fun1(num) :
    if num == 1 :
        return 0
    else :
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0 :
                return 0
        return 1

M = int(input())
N = int(input())

pull = []
for i in range(M, N+1):
    if fun1(i) :
        pull.append(i)

if len(pull) == 0 :
    print(-1)
else :
    print(sum(pull))
    print(pull[0])
