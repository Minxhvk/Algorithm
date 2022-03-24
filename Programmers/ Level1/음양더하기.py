def solution(absolutes, signs):
    answer = 0

    for k, i in enumerate(absolutes):
        if signs[k] == False:
            answer -= i
        else:
            answer += i
    return answer
