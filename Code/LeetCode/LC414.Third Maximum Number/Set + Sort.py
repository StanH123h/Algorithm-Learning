from typing import List


class Solution:
    # 时间复杂度O(nlogn)
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort(reverse=True)
        if len(nums) >= 3:
            return nums[2]
        return nums[0]


a = Solution()
print(a.thirdMax([3, 2, 1]))
