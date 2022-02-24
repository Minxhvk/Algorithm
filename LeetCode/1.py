# Two Sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, m in enumerate(nums):
            if target - m in nums_map:
                return nums_map[target - m], i
            nums_map[m] = i
