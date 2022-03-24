
def solution(n, lost, reserve):

    new_lost = set(lost) - set(reserve)
    new_reserve = set(reserve) - set(lost)
    answer = n - len(new_lost)

    for i in new_lost:
        if i - 1 in new_reserve:
            answer += 1
            new_reserve.remove(i-1)
        elif i + 1 in new_reserve:
            answer += 1
            new_reserve.remove(i+1)

    return answer
