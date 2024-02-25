from typing import List


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        # 思路:尽量要免费获得价值大的糖果，所以每次都买最贵的两个糖，然后再免费获得其次贵的糖
        result = sum(cost)
        if len(cost) < 3:
            return result
        cost.sort(reverse=True)
        for i in range(2, len(cost), 3):
            result -= cost[i]
        return result
