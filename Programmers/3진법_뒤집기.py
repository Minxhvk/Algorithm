def solution(n):
    answer = []
    dec = 0
    while n >= 3:
        answer.append(n % 3)
        n = int(n/3)
    answer.append(n % 3)
    for i in range(len(answer)):
        dec += (3 ** i) * answer.pop()
    return dec


print(solution(45))
