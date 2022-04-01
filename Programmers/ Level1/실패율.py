import collections

# 정확성 96.3


def solution(N, stages):
    answer = []
    rate_dict = collections.defaultdict(int)
    all_challenge = 0
    not_complete = 0

    for idx, val in enumerate(sorted(stages)):
        if val > N:
            val = N
        if rate_dict[val] != 0:
            continue
        all_challenge = len(stages) - idx
        not_complete = stages.count(val)
        rate = not_complete / all_challenge
        rate_dict[val] = rate

    for i in range(1, N+1):
        if rate_dict[i] == 0:
            rate_dict[i] = 0
    for i, j in sorted(rate_dict.items(), key=lambda item: item[1], reverse=True):
        answer.append(i)

    return answer
