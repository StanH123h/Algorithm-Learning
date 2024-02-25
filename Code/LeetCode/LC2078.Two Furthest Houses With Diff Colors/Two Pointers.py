from typing import List


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        # 思路:第一个房子选择头或者尾元素，再对比两个max_dis哪个长,因为最长的组合绝对包含头或者尾元素
        head_color = colors[0]
        current_max_dis = 0
        tail_color = colors[len(colors) - 1]
        # 先从尾部遍历，找到第一个和头部颜色不同的房子为止
        for i in range(len(colors) - 1, -1, -1):
            if colors[i] != head_color:
                current_max_dis = i
                break
        # 再从头部开始遍历，找到第一个和尾部颜色不同的房子
        for i in range(len(colors)):
            if colors[i] != tail_color:
                if (len(colors) - 1 - i) > current_max_dis:
                    return len(colors) - 1 - i
                else:
                    return current_max_dis
