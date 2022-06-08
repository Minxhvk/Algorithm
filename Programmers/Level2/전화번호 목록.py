import heapq


def solution(phone_book):
    # heapq로 정렬되어 전에 값을 비교할 필요가 없다.
    heapq.heapify(phone_book)
    p_num = heapq.heappop(phone_book)

    while phone_book:
        i = len(p_num)
        if p_num == phone_book[0][:i]:
            return False

        p_num = heapq.heappop(phone_book)

    return True
