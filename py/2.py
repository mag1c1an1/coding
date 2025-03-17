#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param houses int整型一维数组
# @param heaters int整型一维数组
# @return int整型
#
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # write code here
        houses.sort()
        heaters.sort()
        heaters = [float("-inf")] + heaters + [float("inf")]
        res = 0
        i = 0
        for house in houses:
            while house > heaters[i + 1]:
                i += 1
            res = max(res, min(house - heaters[i], heaters[i + 1] - house))
        return res


def min_cost_for_car_purchase(X, Y, n, cars):
    # 创建所有可能的配置
    configurations = []
    for car in cars:
        base_price, base_people, base_cargo, options = car
        configurations.append((base_price, base_people, base_cargo))

        for option in options:
            option_price_change, option_people_change, option_cargo_change = option
            total_price = base_price + option_price_change
            total_people = base_people + option_people_change
            total_cargo = base_cargo + option_cargo_change

            if total_price > 0 and total_people > 0 and total_cargo > 0:
                configurations.append((total_price, total_people, total_cargo))

    # 初始化dp数组
    INF = float("inf")
    dp = [[INF] * (Y + 1) for _ in range(X + 1)]
    dp[0][0] = 0

    # 完全背包算法
    for price, people, cargo in configurations:
        for p in range(X + 1):
            for c in range(Y + 1):
                if dp[p][c] != INF:
                    np = min(p + people, X)
                    nc = min(c + cargo, Y)
                    dp[np][nc] = min(dp[np][nc], dp[p][c] + price)

    return dp[X][Y]
