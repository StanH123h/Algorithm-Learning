# 假设背包能装4pounds
#需要保证items至少包含两个数
def optimized_steal(max_capacity,*items):#max_capacity为背包容量，这个参数后面的所有参数都会被打包到一个tuple中
    grid = []
    precision=gcd_more_than_two_items(get_weight_from_items(list(items)))#获取精度，用来制作网格的x轴
    dp_capacity = []  # 用于记录每列背包分别容量为多大
    for i in range(int(max_capacity/precision)):
        dp_capacity.append(precision*(i+1))
    unlocked_items = []  # 用于保存已经“解锁”的物品
    for i in range(len(items)):
        grid.append([0] * len(dp_capacity))  # 初始化网格
    for i_tr in range(len(grid)):
        unlocked_items.append(items[i_tr])
        new_item = items[i_tr]  # 用于记录最新“解锁”的物品
        new_item_weight = new_item[0]  # 最新“解锁”物品的重量
        new_item_value = new_item[1]  # 最新“解锁”物品的价值
        for i_td in range(len(grid[i_tr])):
            new_value = 0  # 最新计算出来的本格价值
            capacity = dp_capacity[i_td]
            if len(unlocked_items) == 1 and new_item_weight <= capacity:
                grid[i_tr][i_td] = new_item_value
            elif new_item_weight <= capacity:
                new_value += new_item_value
                old_value = grid[i_tr - 1][dp_capacity.index(capacity)]  # 上一行本格的价值
                capacity -= new_item_weight
                if capacity > 0:
                    new_value += grid[i_tr - 1][dp_capacity.index(capacity)]  # 如果还有剩下的，就加上上一行的剩余capacity最优解
                if new_value > old_value:
                    grid[i_tr][i_td] = new_value
                else:
                    grid[i_tr][i_td] = old_value
            else:
                grid[i_tr][i_td] = grid[i_tr-1][i_td]
    return grid[len(items) - 1][len(dp_capacity) - 1]


def euclidean_gcd(num1, num2):#Euclidean GCD Algorithm
    big_num = num1 if num1 > num2 else num2
    small_num = num2 if num1 > num2 else num1
    q = big_num // small_num
    r = big_num - small_num * q
    if r == 0:
        return small_num
    else:
        return euclidean_gcd(small_num, r)

def gcd_more_than_two_items(items):#一直GCD两个数，把他们的GCD存到数组中，直到只剩下最后一个数
    items_list = items
    if len(items_list) == 1:
        return items_list[0]
    num1=items_list.pop(0)
    num2=items_list.pop(0)
    items_list.append(euclidean_gcd(num1,num2))
    return gcd_more_than_two_items(items_list)

def get_weight_from_items(items):
    result=[]
    for item in items:
        result.append(item[0])
    return result

print(optimized_steal(2,[0.5,7],[0.5,6],[1,9],[2,9],[0.5,8]))  # index0为重量,index1为价值
