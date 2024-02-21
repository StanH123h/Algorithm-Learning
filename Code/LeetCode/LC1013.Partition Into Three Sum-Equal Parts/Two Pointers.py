from typing import List


class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        summation = sum(arr)
        if summation % 3 != 0:
            return False
        length = len(arr)
        equal_part_num = sum(arr) // 3
        left = [0, 0, None]  # 分别代表[左指针索引,左边部分数字个数,左边部分总和]
        right = [length - 1, 0, None]  # 与left相同
        while left[0] < right[0]:
            if left[2] != equal_part_num:
                left_num = arr[left[0]]
                left[2] = left[2] + left_num if left[2] is not None else left_num
                summation -= left_num
                left[1] += 1
                if left[2] != equal_part_num:
                    left[0] += 1
            if right[2] != equal_part_num:
                right_num = arr[right[0]]
                right[2] = right[2] + right_num if right[2] is not None else right_num
                summation -= right_num
                right[1] += 1
                if right[2] != equal_part_num:
                    right[0] -= 1
            if left[1] + right[1] == len(arr):
                return False
            if left[2] == right[2] == equal_part_num:
                return True
        return False
