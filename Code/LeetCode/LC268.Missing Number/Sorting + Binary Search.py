from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 思路，排序完二分查找直到left>right,然后left代表的索引正好就是缺少的数
        nums.sort()
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] != mid:
                right = mid - 1
            else:
                left = mid + 1
        return left
