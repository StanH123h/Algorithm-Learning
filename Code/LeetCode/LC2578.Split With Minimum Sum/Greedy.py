class Solution:
    def splitNum(self, nums: int) -> int:
        # 思路:选择尽量小的数当作尽量大的位数
        num1=''
        num2=''
        nums='*'.join(str(nums)).split("*")
        nums.sort()
        for i in range(len(nums)):
            if i%2==0:#不断地让两个数的位数变为尽量小的数
                num1+=nums[i]
            else:
                num2+=nums[i]
        return int(num1)+int(num2)
