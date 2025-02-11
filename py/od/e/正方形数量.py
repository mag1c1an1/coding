import sys

# 读取第一个输入的整数，表示坐标数量
n = int(input())

# 存储坐标的字符串形式的列表
coordinates = []
for i in range(n):
    # 读取坐标点的字符串，并去掉两端的空白字符
    coordinates.append(input().strip())

# 初始化正方形计数器
squareCount = 0
# 使用集合存储坐标点，便于快速查找
coordinate_set = set(coordinates)

# 遍历所有坐标点对
for i in range(n):
    # 将第一个坐标点分割为x1和y1
    x1, y1 = map(int, coordinates[i].split())

    for j in range(i + 1, n):
        # 将第二个坐标点分割为x2和y2
        x2, y2 = map(int, coordinates[j].split())

        # 计算两个可能的对角点
        x3, y3 = x1 - (y1 - y2), y1 + (x1 - x2)
        x4, y4 = x2 - (y1 - y2), y2 + (x1 - x2)

        # 检查这两个对角点是否存在于坐标集合中
        if f"{x3} {y3}" in coordinate_set and f"{x4} {y4}" in coordinate_set:
            squareCount += 1

        # 计算另外两个可能的对角点
        x5, y5 = x1 + (y1 - y2), y1 - (x1 - x2)
        x6, y6 = x2 + (y1 - y2), y2 - (x1 - x2)

        # 检查这两个对角点是否存在于坐标集合中
        if f"{x5} {y5}" in coordinate_set and f"{x6} {y6}" in coordinate_set:
            squareCount += 1

# 每个正方形被计算了4次，因此结果需要除以4
print(squareCount // 4)
