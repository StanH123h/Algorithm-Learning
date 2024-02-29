import bisect
from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # 思路:前缀和然后二分查找
        # 思路和贪心的基本一样，但是二分查找会让时间复杂度低很多
        nums.sort()
        summation = nums[0]
        result = []
        for i in range(1, len(nums)):
            temp_num = nums[i]
            nums[i] += summation
            summation += temp_num
        for query in queries:
            result.append(bisect.bisect_right(nums, query))
        return result
