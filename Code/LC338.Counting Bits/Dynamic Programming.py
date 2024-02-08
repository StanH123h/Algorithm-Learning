from typing import List


class Solution:
    #思路:每个十进制数字只相差1，所以只要判断二进制末尾数，然后末尾数如果是1，那就一直进位直到遇到0（所以在开头加0)
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        dp_count1 = [0]
        for i in range(1, n + 1):
            continuous_1_counts = 0
            binary = '0' + str(bin(i - 1))[2::]
            # [2::]是为了去掉二进制转换完的"0b"前缀,最前面加一个"0"是为了防止后面循环时遇到全是"1"的二进制就不append了
            for char in binary[::-1]:
                if char != "1":
                    dp_count1.append(dp_count1[i - 1] - continuous_1_counts + 1)
                    break
                else:
                    continuous_1_counts += 1
        return dp_count1
