from typing import List


class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int],
                         experience: List[int]) -> int:
        # 解题:1.in order表示不能选择oppo顺序2.Strictly Greater
        # 思路:贪心+优化
        result = 0
        total_ener = sum(energy)  # 开始直接计算总共energy进行性能优化
        if total_ener >= initialEnergy:
            result += total_ener + 1 - initialEnergy
        for i in range(len(energy)):
            if initialExperience <= experience[i]:
                diff = experience[i] + 1 - initialExperience
                result += diff
                initialExperience += diff
            initialExperience += experience[i]
        return result
