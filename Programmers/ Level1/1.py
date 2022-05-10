from collections import deque


def solution(atmos):
    answer = deque()
    cnt = 0
    for i, j in atmos:
        if (i > 150) and (j > 75):
            answer.append(2)
        elif (i > 80) or (j > 35):
            answer.append(1)
        else:
            answer.append(0)

    while answer:
        num = answer.popleft()
        if num == 1:
            cnt += 1
            if answer is not None:
                if answer.popleft() == 2:
                    continue
            if answer is not None:
                answer.popleft()
        elif num == 2:
            cnt += 1

    return cnt
