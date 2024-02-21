from typing import List


class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        # 思路:维护一个变量，如果该变量不等于sum(arr)//3就一直往该变量增加新的值，每次该变量等于sum(arr)//3就count++
        total = sum(arr)
        if total % 3 != 0:
            return False
        part_total = total // 3
        temp_total = None
        part_counts = 0
        for num in arr:
            if temp_total is None:
                temp_total = num
            else:
                temp_total += num
            if temp_total == part_total:
                temp_total = None
                part_counts += 1
        return part_counts >= 3  # ">="是为了防止arr中有0且sum(arr)//3也是0导致结果数出来大于3个
