class Solution:
    def minMaxDifference(self, nums: int) -> int:
        # 思路：
        # max:找位数大的数修改成9
        # min:找位数大的数修改成0
        max_digit = None  # 要修改的最大数
        min_digit = None  # 要求改的最小数
        max_num = ""
        min_num = ""
        nums = str(nums)
        for num in nums:
            if max_digit is None and num != "9":
                max_digit = num
            if min_digit is None and num != "0":
                min_digit = num
            if num == max_digit:
                max_num += "9"
            else:
                max_num += num
            if num == min_digit:
                min_num += "0"
            else:
                min_num += num
        return int(max_num) - int(min_num)
