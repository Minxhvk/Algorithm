from collections import defaultdict
import collections
import heapq

# 나의 풀이


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt_list = []
        answer = []
        cnt = defaultdict(str)
        for i in nums:
            if i in cnt:
                continue
            cnt[i] = nums.count(i)
            cnt_list.append(nums.count(i))

        for key, val in cnt.items():
            if val >= sorted(cnt_list, reverse=True)[k-1]:
                answer.append(key)
        return answer

# 책 풀이 1


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.Counter(nums)
        freqs_heap = []

        for f in freqs:
            # 최대 힙 사용을 위해 음수로 설정
            # val, key 로 변경되어 val이 가장 큰 값부터 뽑을 수 있다.
            heapq.heappush(freqs_heap, (-freqs[f], f))
        topk = list()
        for _ in range(k):
            # val이 가장 큰 부분의 key값
            topk.append(heapq.heappop(freqs_heap)[1])
        return topk

# 책 풀이 2


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(zip(*collections.Counter(nums).most_common(k)))[0]
