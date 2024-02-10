from typing import List
#这个import的解释
#Python 运行时不强制执行函数和变量类型注解，但这些注解可用于类型检查器、IDE、静态检查器等第三方工具。
#也就是说你写错了也不会影响程序运行，但是当然不建议这么做。
#此模块为运行时提供类型提示支持。最基本的支持类型包括Any、Union、Callable、TypeVar和Generic。要获得完整的规范，请参阅PEP 484。
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        row = [1, 1]
        for i in range(2, rowIndex + 1):
            mid = i // 2
            half_repeat_row = []
            if i % 2 == 0:
                for i2 in range(1, mid):
                    half_repeat_row.append(row[i2 - 1] + row[i2])
                row = [1] + half_repeat_row + [row[mid - 1] + row[mid]] + list(reversed(half_repeat_row)) + [1]
            else:
                for i2 in range(1, mid + 1):
                    half_repeat_row.append(row[i2 - 1] + row[i2])
                half_repeat_row.extend(reversed(half_repeat_row))
                row = [1] + half_repeat_row + [1]
        return row
