import sys
import heapq

def get():
    return sys.stdin.readline().rstrip()


def solution(test_set):
    
    min_heap = []
    max_heap = []

    temp_answer = []

    for idx, val in enumerate(test_set, 1):
        if len(min_heap) == len(max_heap):
            heapq.heappush(max_heap, -val)
        else:
            heapq.heappush(min_heap, val)

        if min_heap and min_heap[0] < -max_heap[0]:
            min_val = heapq.heappop(min_heap)
            max_val = heapq.heappop(max_heap)

            heapq.heappush(max_heap, -min_val)
            heapq.heappush(min_heap, -max_val)

        if idx % 2 == 1:
            temp_answer.append(-max_heap[0])

    return temp_answer


N = int(get())

for _ in range(N):

    len_case = int(get())

    if len_case > 10:
        test_set = []
        for _ in range(len_case // 10 + 1):
            test_set.extend(list(map(int, get().split(' '))))
    else:
        test_set = list(map(int, get().split(' ')))


    answer = solution(test_set)
    
    len_answer = len(answer)

    print(len_answer)
    for i in range(0, len_answer, 10):
        print(' '.join(map(str, answer[i:i+10])))