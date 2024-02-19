from typing import List


class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        # 难点:题目很难理解
        binary_num = groups[0]
        max_length_substring = [words[0]]
        for i in range(1, len(groups)):
            if groups[i] != binary_num:
                binary_num = groups[i]
                max_length_substring.append(words[i])
        return max_length_substring
