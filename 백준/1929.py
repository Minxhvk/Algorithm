import math

# 소수 구하는 법 : 제곱근까지만 나누어 봐도 된다.

def fun1(num) :
    if num == 1 :
        return 0
    else :
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0 :
                return 0
        return 1

M, N = map(int, input().split())

for i in range(M, N+1):
    if fun1(i) :
        print(i)
