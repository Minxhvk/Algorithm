# array-partition-i

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        result = 0
        for i in range(0,len(nums),2):
            result += min(nums[i], nums[i+1])
            
        return result

## 한줄 풀이
def arrayPairSum(self, nums: List[int]) -> int:
  return sum(sorted(nums)[::2])