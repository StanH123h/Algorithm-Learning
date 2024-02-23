from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # 思路:从第二个数开始遍历，并判断这个数相比于前面那个数的大小
        if len(nums) <= 1:
            return 0
        result = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:  # 之所以是<=因为题目中说"Strictly Inc"
                difference = nums[i - 1] - nums[i]
                nums[i] += difference + 1
                result += difference + 1
        return result
