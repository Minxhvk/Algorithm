import heapq


def solution(jobs):
    start = -1
    now, answer, i = 0, 0, 0

    hq = []

    while i < len(jobs):
        for j in jobs:
            # 전에 시작한 시간보다 크고, 현재 시간보다 작거나 같아야 함
            if start < j[0] <= now:
                # 처리 시간 순으로 min heap 생성
                heapq.heappush(hq, [j[1], j[0]])

        if len(hq) > 0:
            cur = heapq.heappop(hq)
            start = now
            now += cur[0]
            answer += (now - cur[1])
            i += 1
        else:
            now += 1

    return int(answer / len(jobs))
