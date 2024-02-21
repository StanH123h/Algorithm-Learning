from typing import List


class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        # 思路:每次都装目前最轻的苹果
        weight.sort()
        capacity = 5000
        result = 0
        for heaviness in weight:
            if capacity >= heaviness:
                capacity -= heaviness
                result += 1
            else:
                break
        return result
