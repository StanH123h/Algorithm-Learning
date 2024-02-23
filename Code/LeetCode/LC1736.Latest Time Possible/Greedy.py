class Solution:
    def maximumTime(self, time: str) -> str:
        # 思路:先用Greedy根据不同的位置给出该位置可能出现的最晚值，最后再去调整，防止超出限制
        hour, minute = time.split(":")
        result_hour = ""
        result_minute = ""
        available_hour_digits = 0  # 记录hour哪个位置可以改变
        # 0表示不能改,1表示位置1(十位)能改,2表示位置2(个位)能改，3表示都能改
        for digit in range(2):
            if hour[digit] == "?":
                if digit == 0:
                    result_hour += "2"
                    available_hour_digits += 1
                else:
                    result_hour += "9"
                    available_hour_digits += 2
            else:
                result_hour += hour[digit]
            if minute[digit] == "?":
                if digit == 0:
                    result_minute += "5"
                else:
                    result_minute += "9"
            else:
                result_minute += minute[digit]
        if int(result_hour) > 23:  # 防止Greedy出来的hour超过23
            if available_hour_digits == 3 or available_hour_digits == 2:
                result_hour = "23"
            elif available_hour_digits == 1:
                result_hour = "1" + result_hour[1]
        return result_hour + ":" + result_minute
