import math


def solution(progresses, speeds):
    answer = []
    comp_date = []

    for i, j in zip(progresses, speeds):
        comp_date.append(math.ceil((100 - i) / j))  # 남은 개발 일 계산

    local_max = comp_date.pop(0)
    cnt = 1

    for i in comp_date:
        if i > local_max:  # 전 보다 크다면
            local_max = i
            answer.append(cnt)
            cnt = 1
        else:
            cnt += 1

    answer.append(cnt)
    return answer
