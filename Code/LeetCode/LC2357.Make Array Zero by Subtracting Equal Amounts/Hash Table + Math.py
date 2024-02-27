from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # 思路:数一下nums中有几种类型的的非0的数,那就是min operation次数
        # I love Algorithms!!
        exist = {}
        result = 0
        for num in nums:
            if num != 0 and num not in exist.keys():
                exist[num] = True
                result += 1
        return result
