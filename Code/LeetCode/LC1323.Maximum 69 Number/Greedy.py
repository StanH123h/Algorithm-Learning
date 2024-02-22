class Solution:
    def maximum69Number(self, num: int) -> int:
        # 思路:一直遍历到6为止，这样就能保证修改的6是位数最大的6
        str_num = str(num)
        for i in range(len(str_num)):
            if str_num[i] == "6":
                return int(str_num[:i:] + "9" + str_num[i + 1::])
        return num
