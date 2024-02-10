from typing import List


class Solution:
    # 思路:运用异或的特殊性质
    # 异或详解:(../../../Newly Learned)文件夹中
    def missingNumber(self, nums: List[int]) -> int:
        nums2 = []
        for i in range(len(nums) + 1):
            nums2.append(i)
        result = 0
        for num in nums + nums2:
            result = result ^ num
        return result
