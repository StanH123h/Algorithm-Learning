from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # 思路:不断地先存装有最多物品的box
        boxTypes = self.reversed_quick_sort_by_second_item_in_list(boxTypes)  # 其实python的sort方法可以设置key的，当时不知道
        current_box = 0  # 记录遍历到第几种box了
        result = 0
        while truckSize >= 0:
            result += boxTypes[current_box][1] * boxTypes[current_box][0]
            truckSize -= boxTypes[current_box][0]
            current_box += 1
            if current_box == len(boxTypes):
                if truckSize < 0:
                    result -= boxTypes[current_box - 1][1] * (-truckSize)
                return result
        if truckSize < 0:
            result -= boxTypes[current_box - 1][1] * (-truckSize)
        return result

    def reversed_quick_sort_by_second_item_in_list(self, l):
        if len(l) <= 1:
            return l
        base_num = [l[len(l) // 2][1], len(l) // 2]
        smaller = []
        larger = []
        for i in range(len(l)):
            if i != base_num[1]:
                box_size = l[i][1]
                if box_size >= base_num[0]:
                    larger.append(l[i])
                else:
                    smaller.append(l[i])
        return self.reversed_quick_sort_by_second_item_in_list(larger) + [
            l[base_num[1]]] + self.reversed_quick_sort_by_second_item_in_list(smaller)
