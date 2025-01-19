"""
题目描述
入职后，导师会请你吃饭，你选择了火锅。

火锅里会在不同时间下很多菜。

不同食材要煮不同的时间，才能变得刚好合适。

你希望吃到最多的刚好合适的菜，但你的手速不够快，用m代表手速，每次下手捞菜后至少要过m秒才能再捞（每次只能捞一个）。

那么用最合理的策略，最多能吃到多少刚好合适的菜？

输入描述
第一行两个整数n，m，其中n代表往锅里下的菜的个数，m代表手速。（1 < n, m < 1000）

接下来有n行，每行有两个数x，y代表第x秒下的菜过y秒才能变得刚好合适。（1 < x, y < 1000）

输出描述
输出一个整数代表用最合理的策略，最多能吃到刚好合适的菜的数量。

示例1
输入

2 1
1 2
2 1
1
2
3
输出

1
1




"""


def main():
    n, m = map(int, input().split())

    times = []
    for _ in range(n):
        s, d = list(map(int, input().split()))
        times.append(s + d)
    # nums = [0] * (max(times) + 1)
    # for t in times:
    #     nums[t] = 1
    # dp = []

    # def dfs(t, data):
    #     if t >= len(nums):
    #         dp.append(data)
    #         return
    #     if nums[t] == 1:
    #         dfs(t + m, data + 1)
    #         dfs(t + 1, data)
    #     else:
    #         dfs(t + 1, data)

    # dfs(1, 0)
    # print(dp)
    # print(max(dp))

    times.sort()
    cnt = 1
    last_time = times[0]
    for i in range(1, n):
        if times[i] >= last_time + m:
            cnt += 1
            last_time = times[i]
    print(cnt)


if __name__ == "__main__":
    main()
