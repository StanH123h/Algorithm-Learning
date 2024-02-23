class Solution:
    def largestOddNumber(self, nums: str) -> str:
        # 思路:维护两个指针，指向一个区间，右指针遇到奇数时就把这个区间的字符串加到结果中
        # 此方法效率不如Mathematics.py的方法，单纯为了练习Greedy而写的
        left = 0
        result = ""
        for i in range(len(nums)):  # 右指针就是i
            if int(nums[i]) % 2 != 0:
                result += nums[left:i + 1:]
                left = i + 1
        return result
