from typing import List


class Solution:
    def fillCups(self, amount: List[int]) -> int:
        # 思路:贪心:不断地打数量排前二的水
        # 打败100%的用户啦!!!
        result = 0
        while amount != [0, 0, 0]:
            amount.sort(reverse=True)
            amount[0] -= 1
            if amount[1] != 0:
                amount[1] -= 1
            result += 1
        return result
