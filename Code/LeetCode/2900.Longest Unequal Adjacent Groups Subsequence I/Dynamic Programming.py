from typing import List


class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        last_0 = []
        last_1 = []
        for i in range(len(groups)):
            if groups[i] == 0:
                last_1 = last_0 + [words[i]]
            else:
                last_0 = last_1 + [words[i]]
        if len(last_0) >= len(last_1):
            return last_0
        else:
            return last_1
