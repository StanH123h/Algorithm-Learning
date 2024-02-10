solutions = {}


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n in solutions.keys():
            return solutions[n]
        solutions[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)  # 用散列表空间换时间
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
