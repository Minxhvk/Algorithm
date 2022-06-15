import heapq

# 내 풀이


def solution(operations):
    answer = []
    hq = []

    for i in operations:
        if i[0] == "I":
            heapq.heappush(hq, int(i.split()[1]))
        else:
            # 비어 있을 경우
            if(len(hq) == 0):
                continue

            if i[-2] == "-":
                heapq.heappop(hq)
            else:
                hq = heapq.nlargest(len(hq), hq)[1:]
                heapq.heapify(hq)

    if len(hq) == 0:
        return [0, 0]
    else:
        answer = heapq.nlargest(len(hq), hq)
        return [answer[0], answer[-1]]
