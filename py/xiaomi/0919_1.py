# 小明正在整理他的玩具，他遇到了一道有趣的装箱问题:他有一个容量为N的箱子，并且有n个大小为ai的玩具。除了这n个玩具外，还有c个大小均为1的填充物，它们是小明参加各种活动的纪念品，正好可以拿来填充缝隙。他的任务是确定是否可以选其中一些玩具(填充物也包含在内)放入箱子中，恰好装满箱子，而不留下任何空隙，当然，他也可以选择全部用填充物来埴满整个箱子(如果埴充物足够多的话)，也即装满一箱纪念品，小明也觉得很棒!

# 输入:
# 第一行:N,n,c
# 第二行:a1,a2,...,an
# 输出:
# 如果可以装满箱子，输出"YES",否则输出"NO"

N, n, c = map(int, input().split())
if n > 0:
    a = list(map(int, input().split()))
else:
    a = []

# 如果填充物数量足够填满箱子,直接返回YES
if c >= N:
    print("YES")
    exit()

# dp[i][j]表示前i个玩具能否拼出体积j
dp = [[False] * (N + 1) for _ in range(n + 1)]
dp[0][0] = True

# 对每个玩具,可以选择放或不放
for i in range(n):
    for j in range(N + 1):
        if dp[i][j]:
            dp[i + 1][j] = True
            if j + a[i] <= N:
                dp[i + 1][j + a[i]] = True

# 检查是否存在一个体积j,使得j加上剩余的填充物恰好等于N
for j in range(N + 1):
    if dp[n][j] and N - j <= c:
        print("YES")
        exit()

print("NO")
