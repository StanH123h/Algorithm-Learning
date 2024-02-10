from typing import List


class Solution:
    # 运用摩尔投票算法
    # 算法详解:(../../../Newly Learned)文件夹中
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if candidate == num else -1)
        return candidate
