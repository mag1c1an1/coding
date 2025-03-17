from bisect import bisect
from functools import cache
from itertools import accumulate
import heapq
from math import inf
from collections import Counter, defaultdict, deque
from typing import List


class Item:
    def __init__(self, a, b):
        self.min = a * 60 + b

    def __lt__(self, other):
        return self.min < other.min


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param timePoints string字符串一维数组
# @return int整型
#
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # write code here
        lst = []
        for time in timePoints:
            a, b = map(int, time.split(":"))
            print(a, b)
            lst.append(Item(a, b))
            if a == 0:
                lst.append(Item(24, 0))
        lst.sort()
        ans = inf
        for l in range(len(lst) - 1):
            ans = min(ans, lst[l + 1].min - lst[l].min)
        return ans


x = ["23:59", "00:00"]
y = Solution().findMinDifference(x)
print(y)
