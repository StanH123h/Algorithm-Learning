from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if s==[]:
            return 0
        g.sort()
        s.sort()
        result=0
        for i in range(len(g)):
            while s[0]<g[i]:
                s.pop(0)
                if s==[]:
                    return result
            result+=1
            s.pop(0)
            if s==[]:
                return result
        return result
