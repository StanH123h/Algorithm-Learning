from typing import List


class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        # 思路:拥有最大的index为0的数的数组就是最大的subarray
        # 但是前提条件是该数后面的数能够让这个subarray达到K的长度
        if k == 1:
            return [max(nums)]
        largest_acceptable_num_index = nums.index(max(nums[:-k + 1:]))
        return nums[largest_acceptable_num_index:largest_acceptable_num_index + k:]
