from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 思路:先排序，这样相同的数字就会连续出现，让后跳每次对比当前元素和当前元素索引+数组长度/2,如果二者相同，就能说明该元素为major element
        # 这里不需要考虑该元素不存在的情况，因为题目说明了该元素一定存在
        # 更优的算法:摩尔投票算法，见此文件夹的另一个文件
        length = len(nums)
        if length == 1:
            return nums[0]
        nums.sort()
        length = len(nums)
        majority_times = length // 2
        current_num = nums[0]
        for i in range(length - majority_times):
            if nums[i + majority_times] == current_num:
                return current_num
            else:
                current_num = nums[i + 1]
