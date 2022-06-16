def solution(name):
    answer = 0

    for i in range(len(name)):
        move = 0
        cur = 0
        answer += min((ord(name[i]) - ord('A')),
                      (ord('A') - ord(name[i]) + 26))
        if name[i] != 'A':
            move = i - cur
            cur = i
        if name[-i] != 'A':
            move = i - cur
            cur = i
        # 하.. 머라는거야 도대체...

        answer +=

    return answer
