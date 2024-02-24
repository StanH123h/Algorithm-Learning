class Solution:
    def minTimeToType(self, word: str) -> int:
        # 思路:正序倒序中不断选距离短的
        clockwise = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
                     'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23,
                     'x': 24, 'y': 25, 'z': 26}
        current = 'a'
        result = 0
        for char in word:
            if current == char:
                result += 1
            else:
                clockwise_span = abs(clockwise[char] - clockwise[current])
                counter_clockwise_span = 26 - clockwise_span
                result += min(counter_clockwise_span, clockwise_span)
                result += 1
                current = char
        return result
