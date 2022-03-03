def solution(answers):
    answer = []
    cnt = []
    no1 = [1, 2, 3, 4, 5] * int(len(answers))
    no2 = [2, 1, 2, 3, 2, 4, 2, 5] * int(len(answers))
    no3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * int(len(answers))

    for i in range(len(answers)):
        if answers[i] == no1[i]:
            no1[i] = 0
        if answers[i] == no2[i]:
            no2[i] = 0
        if answers[i] == no3[i]:
            no3[i] = 0

    answer.append(no1.count(0))
    answer.append(no2.count(0))
    answer.append(no3.count(0))
    for i in range(len(answer)):
        if answer[i] == max(answer):
            cnt.append(i+1)
    return cnt
