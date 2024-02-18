from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        # 思路:如果是"I"，要比下一个小，那就从可选数中选择最小的，如果是"D"就选最大的
        if s == "I":
            return [0, 1]
        elif s == "D":
            return [1, 0]
        available = []
        result = []
        for i in range(len(s) + 1):
            available.append(i)
        for char in s:
            if char == "D":
                result.append(available[-1])
                available.pop(-1)
            else:
                result.append(available[0])
                available.pop(0)
        result.extend(available)
        return result
