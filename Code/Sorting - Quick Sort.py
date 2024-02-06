import random  # 导入random模块，用于生成随机数

a = [10, 2, 1, 3, 5, 4, 0, 9, 6, 8, 7]  # 初始化一个列表

# 定义快速排序函数
def quick_sort(l):
    if len(l) <= 1:  # 如果列表长度小于或等于1，无需排序，直接返回
        return l
    bigger = []  # 用于存储所有大于基准数的元素
    smaller = []  # 用于存储所有小于等于基准数的元素
    # 随机选择一个元素作为基准数，并从列表中移除
    base_num = l.pop(random.randint(0, len(l) - 1))
    for item in l:  # 遍历列表中的元素
        if item > base_num:  # 如果元素大于基准数
            bigger.append(item)  # 加入到bigger列表
        else:  # 如果元素小于等于基准数
            smaller.append(item)  # 加入到smaller列表
    # 递归调用quick_sort对smaller和bigger列表进行排序，并将排序结果与基准数合并返回
    return quick_sort(smaller) + [base_num] + quick_sort(bigger)

print(quick_sort(a))
