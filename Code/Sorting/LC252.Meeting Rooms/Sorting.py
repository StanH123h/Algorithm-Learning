from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # 思路:先排序，然后对比前一个的结束时间和后一个的开始时间
        if len(intervals) <= 1:
            return True
        intervals.sort()
        prev_end_time = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < prev_end_time:
                return False
            else:
                prev_end_time = intervals[i][1]
        return True
