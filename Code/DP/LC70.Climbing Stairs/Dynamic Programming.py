class Solution:
    def climbStairs(self, n: int) -> int:
        # 子问题:如何从3开始求出每个台阶数的走法?
        # 思路:因为只能走两格或者一格，所以有n个台阶时的走法=(n-1个台阶时的走法)+(n-2个台阶时的走法)
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        pre_2 = [1, 2]
        for i in range(2, n):
            pre_2.append(pre_2[1] + pre_2.pop(0))
        return pre_2[1]
