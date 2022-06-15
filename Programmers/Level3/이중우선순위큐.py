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

# max_heap, min_heap 따로 구현
# 프로그래머스 다른 사람 풀이


def solution(arguments):
    max_heap = []
    min_heap = []

    for arg in arguments:
        if arg == "D 1":
            if max_heap != []:
                heapq.heappop(max_heap)
                if max_heap == [] or -max_heap[0] < min_heap[0]:
                    min_heap = []
                    max_heap = []
        elif arg == "D -1":
            if min_heap != []:
                heapq.heappop(min_heap)
                if min_heap == [] or -max_heap[0] < min_heap[0]:
                    max_heap = []
                    min_heap = []
        else:
            num = int(arg[2:])
            heapq.heappush(max_heap, -num)
            heapq.heappush(min_heap, num)
    if min_heap == []:
        return [0, 0]
    return [-heapq.heappop(max_heap), heapq.heappop(min_heap)]
