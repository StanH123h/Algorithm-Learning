from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 思路，存在哈希表内，空间换时间
        exist_table = {}
        result = []
        for num in nums1:
            exist_table[num] = True
        for num in nums2:
            if exist_table.get(num):
                result.append(num)
                exist_table[num] = False
        return result
