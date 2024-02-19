from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 思路:维护一个DP数组，代表走到每一格分别需要的最小花费
        min_cost = cost[:2:]  # 前两步的最小花费就是cost中的前两位
        for i in range(2, len(cost)):
            min_cost.append(min(min_cost[i - 1], min_cost[i - 2]) + cost[i])  # 计算这一步的最小花费
        return min(min_cost[-1], min_cost[-2])
