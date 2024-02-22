class Solution:
    def balancedStringSplit(self, s: str) -> int:
        # 思路:一直凑到L的数量=R的数量为止
        current_string = [0, 0]  # [L的数量,R的数量]
        result = 0
        for char in s:
            if char == "L":
                current_string[0] += 1
            else:
                current_string[1] += 1
            if current_string[0] == current_string[1] and current_string[0] != 0:
                result += 1
                current_string = [0, 0]
        return result
