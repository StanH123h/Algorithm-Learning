class Solution:
    def validPalindrome(self, s: str) -> bool:
        # 思路:不断判断删掉左/右字符后剩下的是不是回文
        if len(s) <= 2:
            return True
        left = 0
        right = len(s) - 1
        can_delete = True
        while left <= right:
            if left == right:
                break
            elif s[left] == s[right]:
                left += 1
                right -= 1
            elif not can_delete:
                return False
            elif self.isPalindrome(s[left + 1:right + 1:]):
                left += 1
                can_delete = False
            elif self.isPalindrome(s[left:right:]):
                right -= 1
                can_delete = False
            elif can_delete and right - left <= 1:
                return True
            else:
                return False
        return True

    def isPalindrome(self, s: str) -> bool:
        mid = len(s) // 2
        left = s[:mid:]
        if len(s) % 2 == 0:
            right = s[:mid - 1:-1]
        else:
            right = s[-1:mid:-1]
        return left == right
