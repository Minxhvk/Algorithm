import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    while (scoville[0] < K) and len(scoville) > 1:
        heapq.heappush(scoville, (heapq.heappop(
            scoville)+(heapq.heappop(scoville)*2)))
        cnt += 1
    if scoville[0] < K:
        return -1
    return cnt
