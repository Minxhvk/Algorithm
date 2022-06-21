from collections import deque

# 나의 풀이


def solution(people, limit):
    cnt = 0
    people.sort(reverse=True)
    people = deque(people)

    while (len(people) > 1):
        cur = people.popleft()

        if cur + people[-1] <= limit:
            people.pop()

        cnt += 1
    if len(people) == 0:
        return cnt
    else:
        return cnt+1

# 다른 풀이
# 짝이 지어졌을 경우에만 두명씩 빠지므로 len(people) - answer로 정답을 구할 수 있다.


def solution(people, limit):
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b:
        if people[b] + people[a] <= limit:
            a += 1
            answer += 1
        b -= 1

    return len(people) - answer
