class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
                if nums[mid-1] < target:
                    return mid
            else:
                start = mid + 1
                if start >= len(nums) or nums[start] > target:
                    return mid+1
        return mid