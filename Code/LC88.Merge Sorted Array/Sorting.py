from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if len(nums1) == m:
            return
        new_nums1 = []
        nums1_index = 0
        nums2_index = 0
        for i in range(m + n):
            if nums1_index == m:
                new_nums1.extend(nums2[nums2_index:n:])
                nums1.clear()
                nums1.extend(new_nums1)
                break
            if nums2_index == n:
                new_nums1.extend(nums1[nums1_index:m:])
                nums1.clear()
                nums1.extend(new_nums1)
                break
            if nums1[nums1_index] >= nums2[nums2_index]:
                new_nums1.append(nums2[nums2_index])
                nums2_index += 1
            else:
                new_nums1.append(nums1[nums1_index])
                nums1_index += 1
