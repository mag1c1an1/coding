from typing import List


def stoneGame(a: List[int]):
    n = len(a)
    dp = [[0] * n for _ in range(n)]
    presum = [0] * (n + 1)
    for i in range(n):
        presum[i + 1] = presum[i] + a[i]
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float("inf")
            for m in range(i, j):
                dp[i][j] = min(
                    dp[i][j], dp[i][m] + dp[m + 1][j] + presum[j + 1] - presum[i]
                )
    return dp[0][n - 1]


def stoneGame2(a: List[int]):
    n = len(a)
    dp = [[0] * n for _ in range(n)]
    presum = [0] * (n + 1)
    for i in range(n):
        presum[i + 1] = presum[i] + a[i]

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if j - i >= 1:
                dp[i][j] = float("inf")
                for m in range(i, j):
                    dp[i][j] = min(
                        dp[i][j], dp[i][m] + dp[m + 1][j] + presum[j + 1] - presum[i]
                    )

    return dp[0][n - 1]


print(stoneGame([4, 1, 1, 4]))
print(stoneGame2([4, 1, 1, 4]))
