# reverse-string

class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()

# 투포인터 방식도 있음


left = 0
right = len(s) - 1

while left < right:
    s[left], s[right] = s[right], s[left]
    left += 1
    right -= 1
