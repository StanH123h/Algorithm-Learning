from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        # 思路:统计奇数索引和偶数索引的chips数量之和，返回小的那一个
        odd_count = 0
        even_count = 0
        for pos in position:
            if pos % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        return min(even_count, odd_count)
