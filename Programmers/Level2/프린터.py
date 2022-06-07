

from collections import deque


def solution(priorities, location):
    answer = 0
    priorities = deque(priorities)

    while(len(priorities) != 0):
        if location == 0:
            if priorities[0] < max(priorities):
                priorities.append(priorities.popleft())
                location = len(priorities) - 1
            else:
                return (answer+1)

        else:
            if priorities[0] < max(priorities):
                priorities.append(priorities.popleft())
                location -= 1
            else:
                priorities.popleft()
                location -= 1
                answer += 1
    return answer

# 다른 풀이


def solution(priorities, location):
    answer = 0
    deq = deque([(i, p) for i, p in enumerate(priorities)])

    while True:
        cur = deq.popleft()
        if any(cur[1] < q[1] for q in deq):
            deq.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
