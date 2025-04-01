from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s = [0] * (len(nums) + 1)
        for i, x in enumerate(nums):
            s[i + 1] = s[i] + x
        ans = 0
        cnt = defaultdict(int)
        # 计算左端点个数
        for sj in s:
            ans += cnt[sj - k]
            cnt[sj] += 1
        return ans
