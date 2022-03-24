# 테스트 50, 효율 0
def solution(participant, completion):
    answer = ''
    for i in participant:
        if i in completion:
            completion.remove(i)
        else:
            answer = i
    return answer

# 테스트 50, 효율 50


def solution(participant, completion):
    for i, j in zip(sorted(participant), sorted(completion)):
        if i != j:
            return i
    return sorted(participant).pop()

# 해시풀이 (구글링)


def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer
