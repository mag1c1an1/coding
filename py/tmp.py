import sys
import math


def main():
    X, Y, n = map(int, sys.stdin.readline().split())
    INF = math.inf
    dp = [[INF] * (Y + 1) for _ in range(X + 1)]
    dp[0][0] = 0
    for _ in range(n):
        m_i, x_i, y_i, K_i = map(int, sys.stdin.readline().split())
        options = [(m_i, x_i, y_i)]
        for __ in range(K_i):
            m_ji, x_ji, y_ji = map(int, sys.stdin.readline().split())
            options.append((m_i + m_ji, x_i + x_ji, y_i + y_ji))

        # 处理分组背包
        tmp = [row[:] for row in dp]
        for cost, dx, dy in options:
            for x in range(X + 1):
                for y in range(Y + 1):
                    if dp[x][y] == INF:
                        continue
                    new_x = min(x + dx, X)
                    new_y = min(y + dy, Y)
                    if dp[x][y] + cost < tmp[new_x][new_y]:
                        tmp[new_x][new_y] = dp[x][y] + cost
        # 更新dp
        for x in range(X + 1):
            for y in range(Y + 1):
                if tmp[x][y] < dp[x][y]:
                    dp[x][y] = tmp[x][y]

    print(dp[X][Y] if dp[X][Y] != INF else -1)


if __name__ == "__main__":
    main()
