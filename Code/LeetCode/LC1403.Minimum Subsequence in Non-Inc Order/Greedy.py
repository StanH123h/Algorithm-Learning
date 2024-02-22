from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        # 题目要求:1.优先最短2.其次最大3.严格大于
        # 思路:保证了sum最大其实就是保证了这个substring是最短的,维护两个变量,
        # 一个表示目前选中的元素的sum,另一个表示剩下的元素的sum
        nums.sort(reverse=True)
        substring_sum = 0
        remnant_sum = sum(nums)
        for i in range(len(nums)):
            substring_sum += nums[i]
            remnant_sum -= nums[i]
            if substring_sum > remnant_sum:
                return nums[:i + 1:]
        return nums
