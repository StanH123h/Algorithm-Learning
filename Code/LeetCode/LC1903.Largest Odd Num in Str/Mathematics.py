class Solution:
    def largestOddNumber(self, nums: str) -> str:
        # 思路:从后往前遍历，直到找到一个oddnum
        for i in range(len(nums) - 1, -1, -1):  # 倒序遍历
            if int(nums[i]) % 2 != 0:
                return nums[:i + 1:]
        return ""
