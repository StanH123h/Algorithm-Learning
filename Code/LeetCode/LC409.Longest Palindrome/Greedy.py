class Solution:
    def longestPalindrome(self, s: str) -> int:
        # 思路:不断找能成对的字母，直到找不到，如果还剩下字母最后+1
        letters_count = {}
        result = 0
        for char in s:
            if char not in letters_count.keys():
                letters_count[char] = 1
            else:
                letters_count[char] += 1
                if letters_count[char] == 2:
                    letters_count[char] = 0
                    result += 2
        for values in letters_count.values():  # 查看最后还有没有剩下的字母
            if values >= 1:
                return result + 1
        return result
