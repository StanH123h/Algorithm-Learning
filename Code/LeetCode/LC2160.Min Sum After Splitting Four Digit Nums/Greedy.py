class Solution:
    def minimumSum(self, num: int) -> int:
        # 思路:首先一定是拆成22分才能让sum尽量小，其次，每次都用最小的数当10位最大的数当个位
        num_list = []
        for i in range(3):
            num_list.append(num % 10)
            num //= 10
        num_list.append(num)
        num_list.sort()
        return int(str(num_list[0]) + str(num_list[-1])) + int(str(num_list[1]) + str(num_list[-2]))
