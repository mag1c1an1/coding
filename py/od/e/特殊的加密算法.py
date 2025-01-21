# 有一种特殊的加密算法，明文为一段数字串，经过密码本查找转换，生成另一段密文数字串。

# 规则如下：

# 明文为一段数字串由 0~9 组成

# 密码本为数字 0~9 组成的二维数组

# 需要按明文串的数字顺序在密码本里找到同样的数字串，密码本里的数字串是由相邻的单元格数字组成，上下和左右是相邻的，注意：对角线不相邻，同一个单元格的数字不能重复使用。

# 每一位明文对应密文即为密码本中找到的单元格所在的行和列序号（序号从0开始）组成的两个数宇。

# 如明文第 i 位 Data[i] 对应密码本单元格为 Book[x][y]，则明文第 i 位对应的密文为X Y，X和Y之间用空格隔开。

# 如果有多条密文，返回字符序最小的密文。

# 如果密码本无法匹配，返回"error"。

# 请你设计这个加密程序。

# 示例1：

# 密码本：

# 0 0 2

# 1 3 4

# 6 6 4

# 明文：“3”，密文：“1 1”

# 示例2：

# 密码本：

# 0 0 2

# 1 3 4

# 6 6 4

# 明文：“0 3”，密文：“0 1 1 1”

# 示例3：

# 密码本：

# 0 0 2 4

# 1 3 4 6

# 3 4 1 5

# 6 6 6 5

# 明文：“0 0 2 4”，密文：“0 0 0 1 0 2 0 3” 和 “0 0 0 1 0 2 1 2”，返回字典序最小的"0 0 0 1 0 2 0 3"

# 明文：“8 2 2 3”，密文：“error”，密码本中无法匹配

# 输入描述
# 第一行输入 1 个正整数 N，代表明文的长度（1 ≤ N ≤ 200）

# 第二行输入 N 个明文组成的序列 Data[i]（0 ≤ Data[i] ≤ 9）

# 第三行输入 1 个正整数 M，代表密文的长度

# 接下来 M 行，每行 M 个数，代表密文矩阵

# 输出描述
# 输出字典序最小密文，如果无法匹配，输出"error"


n = int(input())

data = list(map(int, input().split()))
m = int(input())
book = [list(map(int, input().split())) for _ in range(m)]

OFFSET = [(0, 1), (1, 0), (-1, 0), (0, -1)]
min_path = None
found = False


def dfs(data, index, x, y, visited, path):
    global min_path, found

    if index == len(data):
        if not found or path < min_path:
            min_path = path
        found = True
        return

    if x < 0 or y < 0 or x >= m or y >= m or visited[x][y] or book[x][y] != data[index]:
        return

    visited[x][y] = True
    new_path = path + f"{x} {y} "

    for dir in OFFSET:
        nx, ny = x + dir[0], y + dir[1]
        dfs(data, index + 1, nx, ny, visited, new_path)

    visited[x][y] = False


visited = [
    [False for _ in range(m)] for _ in range(m)
]  # 标记密码本中的数字是否已经被访问过
for i in range(m):
    for j in range(m):
        if book[i][j] == data[0]:  # 从找到的第一个数字开始搜索
            dfs(data, 0, i, j, visited, "")  # 使用深度优先搜索找到所有可能的加密路径

print(
    min_path.strip() if found else "error"
)  # 如果找到至少一种加密方式，输出最小字典序的密文；否则，输出"error"
