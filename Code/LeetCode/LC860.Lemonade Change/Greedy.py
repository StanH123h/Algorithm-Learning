from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # 思路:能找大的零钱就先一直找大的
        changes = {5: 0, 10: 0}
        for bill in bills:
            if bill != 20:
                changes[bill] += 1
            if bill != 5:
                bill -= 5
                while bill >= 10 and changes[10] > 0:
                    bill -= 10
                    changes[10] -= 1
                while bill >= 5 and changes[5] > 0:
                    bill -= 5
                    changes[5] -= 1
                if bill > 0:
                    return False
        return True
