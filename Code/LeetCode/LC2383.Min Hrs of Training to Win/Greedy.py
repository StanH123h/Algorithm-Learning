from typing import List


class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int],
                         experience: List[int]) -> int:
        # 解题:1.in order表示不能选择oppo顺序2.Strictly Greater
        # 思路:贪心(只有不够大了再训练)
        result = 0
        for i in range(len(energy)):
            if initialEnergy <= energy[i] and initialExperience <= experience[i]:
                ener_diff = energy[i] + 1 - initialEnergy
                exp_diff = experience[i] + 1 - initialExperience
                total_diff = ener_diff + exp_diff
                result += total_diff
                initialExperience += exp_diff
                initialEnergy += ener_diff
            elif initialEnergy <= energy[i]:
                ener_diff = energy[i] + 1 - initialEnergy
                result += ener_diff
                initialEnergy += ener_diff
            elif initialExperience <= experience[i]:
                exp_diff = experience[i] + 1 - initialExperience
                result += exp_diff
                initialExperience += exp_diff
            initialEnergy -= energy[i]
            initialExperience += experience[i]
        return result
