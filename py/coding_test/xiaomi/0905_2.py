# 给一个长度为n的序列和一个整数x，每次操作可以选择序列中的一个元素，将其从序列中删去或者将其值加一。问至少操作多少次，可以使操作后的序列(可以为空)中数字之和是x的倍数。
n, x = map(int, input().split())
a = list(map(int, input().split()))
s = sum(a)
if s == 0:
    print(0)
    exit()

# dp[i][j] 表示前i个数,余数为j时的最小操作次数
dp = [[float("inf")] * x for _ in range(n + 1)]
dp[0][0] = 0

for i in range(n):
    for j in range(x):
        if dp[i][j] == float("inf"):
            continue

        # 删除当前数
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)

        # 保留当前数
        new_j = (j + a[i]) % x
        dp[i + 1][new_j] = min(dp[i + 1][new_j], dp[i][j])

        # 加1
        new_j = (j + a[i] + 1) % x
        dp[i + 1][new_j] = min(dp[i + 1][new_j], dp[i][j] + 1)

print(dp[n][0])
