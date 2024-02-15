from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # 思路:能插入花就一直插入
        pre = None
        for i in range(len(flowerbed)):
            after = (flowerbed[i + 1] if i + 1 < len(flowerbed) else None)
            current = flowerbed[i]
            if current == 0 and (pre == None or pre == 0) and (after == None or after == 0):
                pre = 1
                n -= 1
            else:
                pre = current
        return n <= 0
