from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        #思路:不断选择最大的两个数组和在一起
        result=0
        nums.sort()
        for i in range(len(nums)//2):
            max_num1=nums[0]
            nums.pop(0)
            nums.pop(0)
            result+=max_num1
        return result