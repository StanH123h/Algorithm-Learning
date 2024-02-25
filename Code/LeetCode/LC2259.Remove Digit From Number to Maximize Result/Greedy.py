class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        # 思路:先遍历一遍字符串，寻找digit,并判断digit和其后面数的关系
        # 因为如果后面的数比digit大，那么肯定是要删这种digit的,这样才能让删除后的整体变大
        # 优先删除:靠前，后面数比前面大的digit
        # 如果所有digit都比后面的数大，那就尽量删靠后digit
        str_digit = digit
        digit = int(digit)
        last_digit = None  # 记录最后一个出现的digit的位置
        for i in range(len(number)):
            if number[i] == str_digit:
                last_digit = i
                if i != (len(number) - 1) and int(number[i + 1]) > digit:
                    return number[:i:] + number[i + 1::]
        return number[:last_digit:] + number[last_digit + 1::]
