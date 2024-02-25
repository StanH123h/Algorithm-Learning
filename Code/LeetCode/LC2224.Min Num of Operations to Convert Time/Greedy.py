class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        # 思路:先计算出差了多少分钟，再贪心:每次尽量先用大的interval再依次往下减
        # 题中说current<=correct所以不考虑倒着转的问题
        current = current.split(":")
        correct = correct.split(":")
        diff = 0
        for i in range(2):
            if i == 0:
                diff += (int(correct[i]) - int(current[i])) * 60
            else:
                diff += (int(correct[i]) - int(current[i]))
        result = 0
        # 先选60
        operations = diff // 60
        result += operations
        diff -= operations * 60
        # 其次是15
        operations = diff // 15
        result += operations
        diff -= operations * 15
        # 然后是5
        operations = diff // 5
        result += operations
        diff -= operations * 5
        # 最后是1
        return result + diff
