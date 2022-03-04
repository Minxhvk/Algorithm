import collections


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        cnt = 0
        dic = {}

        for j in stones:
            if j not in dic:
                dic[j] = 1
            else:
                dic[j] += 1

        for i in jewels:
            if i in dic:
                cnt += dic[i]
        return cnt


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dic = collections.defaultdict(int)
        cnt = 0

        for i in stones:
            dic[i] += 1

        for j in jewels:
            cnt += dic[j]
        return cnt


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dic = collections.Counter(stones)
        cnt = 0

        for i in jewels:
            cnt += dic[i]
        return cnt


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(s in jewels for s in stones)
