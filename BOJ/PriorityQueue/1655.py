import sys
import heapq

"""
max_heap의 root가 기준이 된다.

"""

def get():
    return sys.stdin.readline().rstrip()

def solution(idx, val):
    
    if len(min_heap) == len(max_heap):
        heapq.heappush(max_heap, -val)
    else:
        heapq.heappush(min_heap, val)

    # 1,2,3,4 에서 7이 들어올 경우, min_heap에 있어야 한다.
    if min_heap and min_heap[0] < -max_heap[0]:
        min_val = heapq.heappop(min_heap)
        max_val = heapq.heappop(max_heap)

        heapq.heappush(min_heap, -max_val)
        heapq.heappush(max_heap, -min_val)

    if idx % 2 == 0:
        return min(-max_heap[0], min_heap[0])
    else:
        return -max_heap[0]


N = int(get())
min_heap = []
max_heap = []

for i in range(N):
    target = int(get())

    print(solution(i+1, target))

