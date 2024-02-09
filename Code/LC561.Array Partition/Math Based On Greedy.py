from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        #思路:因为贪心的思路是不断地获取目前数组中两个最大的值，然后取最小值，所以可以先排序然后排序完后其实偶数索引的就是最小值
        #这样时间复杂度比纯贪心算法更快
        nums = sorted(nums)
        ans = 0
        for i in range(0, len(nums), 2):
            ans += nums[i]
        return ans