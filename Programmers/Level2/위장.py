from collections import defaultdict
from itertools import combinations

# 내 풀이 : 1번 시간 초과


def solution(clothes):
    answer = 0
    clothes_dict = defaultdict(int)

    for _, i in clothes:
        clothes_dict[i] += 1

    cnt_list = clothes_dict.values()

    for i in range(1, len(clothes_dict) + 1):
        combi_list = list(combinations(cnt_list, i))
        for j in range(len(combi_list)):
            tot = 1
            for k in range(len(combi_list[0])):
                tot = tot * combi_list[j][k]
            answer += tot

    return answer

# 개선 풀이


def solution(clothes):
    answer = 1
    clothes_dict = defaultdict(int)

    for _, i in clothes:
        clothes_dict[i] += 1

    for c in clothes_dict.values():
        answer *= c + 1

    return answer - 1
