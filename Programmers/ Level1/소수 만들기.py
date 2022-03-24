import math
from itertools import combinations


def solution(nums):
    answer = 0

    for i in list(combinations(nums, 3)):
        for j in range(2, int(math.sqrt(sum(i)) + 1)):
            if(sum(i) % j == 0):
                break
        else:
            answer += 1

    return answer
