class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # 基于贪心算法实现
        if s == "":
            return True
        current_index = 0
        for char in t:
            if char == s[current_index]:
                current_index += 1
            if current_index == len(s):
                return True
        return len(s) == current_index
