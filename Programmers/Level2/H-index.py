
# 나의 풀이 (O(n^2))
def solution(citations):
    answer = 0
    citations.sort()

    for i in range(1, citations[-1] + 1):
        cnt = 0
        for j in citations:
            if i <= j:
                cnt += 1
        if cnt >= i:
            answer = i

    return answer


# O(n)풀이
def solution(citations):
    citations.sort()
    n = len(citations)

    for i in range(n):
        h_index = n - i

        if citations[i] >= h_index:
            return h_index

    return 0
