"""
题目描述
某个充电站，可提供 n 个充电设备，每个充电设备均有对应的输出功率。

任意个充电设备组合的输出功率总和，均构成功率集合 P 的 1 个元素。

功率集合 P 的最优元素，表示最接近充电站最大输出功率 p_max 的元素。

输入描述
输入为 3 行：

第 1 行为充电设备个数 n
第 2 行为每个充电设备的输出功率
第 3 行为充电站最大输出功率 p_max
备注
充电设备个数 n > 0
最优元素必须小于或等于充电站最大输出功率 p_max
输出描述
功率集合 P 的最优元素

示例1
输入

4
50 20 20 60
90
1
2
3
输出

90
1

"""


def main():
    n = int(input())
    v = list(map(int, input().split()))
    p_max = int(input())
    dp = [0] * (p_max + 1)

    for i in range(n):
        for j in range(p_max, v[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - v[i]] + v[i])

    print(dp[-1])


if __name__ == "__main__":
    main()
