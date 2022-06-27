import math


def solution(n, a, b):
    answer = 0
    N = int(math.log2(n))

    for i in range(N):
        a = math.ceil(a/2)
        b = math.ceil(b/2)
        if (a == b):
            return answer + 1
        answer += 1
