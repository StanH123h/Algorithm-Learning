from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # 思路:先倒序排序，然后获得一个sum(nums),
        # 接下来制作summations用于保存每个长度的子字符串所需要的最小sum
        nums.sort(reverse=True)
        summation = sum(nums)
        summations = [summation]
        result = []
        for i in range(1, len(nums)):
            summation -= nums[i - 1]
            summations.append(summation)
        for query in queries:
            for i in range(len(summations)):
                if i == (len(summations) - 1) and query < summations[i]:
                    result.append(0)
                    break
                elif query >= summations[i]:
                    result.append(len(summations) - i)
                    break
        return result
