import queue

# Graph = {
#     "start": {"a": 6, "b": 2},
#     "a": {"end": 1},
#     "b": {"a": 3, "end": 5},
#     "end": {}
# }
# 最短路径:['start','b','a','end']
# 总成本6
# Graph = {
#     "start": {"a": 2, "b": 5},
#     "a": {"c": 8, "d": 4},
#     "b": {"d": 2},
#     "c": {"end": 6},
#     "d": {"end": 3},
#     "end": {}
# }
# 最短路径：['start', 'a', 'd', 'end']
# 总成本：9
Graph = {
    "start": {"a": 2, "b": 5},
    "a": {"c": 4, "b": 1},
    "b": {"a": 3, "d": 2},
    "c": {"end": 6, "d": 2},
    "d": {"c": 1, "end": 1},
    "end": {}
}
# 最短路径：['start', 'a', 'b', 'd', 'end']
# 总成本：6

# 初始化存储节点成本、父节点和已访问节点的字典
cost = {}
parent = {}
used = {}

# 设置当前节点为起点
current = "start"

# 初始化用于追踪最小成本和对应键的变量
min = None
min_key = None

# 初始化所有节点的成本为一个非常大的数，除了起点，其成本设置为0
for item in Graph.keys():
    cost[item] = 99999999
cost["start"] = 0

# 循环直到当前节点是终点
while current != "end":
    iter_list = []  # 用于存储未处理的节点
    for key, value in Graph[current].items():
        route = 0
        # 如果节点是新发现的，设置其父节点为当前节点
        if key not in parent.keys():
            parent[key] = current
        # 累加从当前节点到邻居节点的成本
        route += Graph[current][key]
        if current != "start":
            # 如果当前节点不是起点，加上从起点到当前节点的成本
            route += cost[current]
        # 如果找到了一条更短的路径到邻居节点，更新其成本和父节点
        if route < cost[key]:
            cost[key] = route
            parent[key] = current
    # 标记当前节点为已处理
    used[current] = True

    # 找出所有未处理的节点，准备下一次迭代
    for key, value in cost.items():
        if key not in used.keys():
            iter_list.append(key)
    # 从未处理的节点中找到成本最低的节点
    min = cost[iter_list[0]]
    min_key = iter_list[0]
    for key in iter_list:
        if cost[key] < min:
            min_key = key
    # 更新当前节点为成本最低的节点，进行下一轮循环
    current = min_key
    min_key = None
    min = None

# 当找到终点后，回溯构建最短路径
current = "end"
result = []
route = cost['end']  # 获取到终点的总成本
while current in parent.keys():
    result.append(current)
    current = parent[current]
result.append("start")
result.reverse()  # 反转列表，因为我们是从终点回溯到起点

# 打印最短路径和总成本
print(result)
print(route)

