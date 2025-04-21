from typing import List


class Solution:
    def masSubArrayLen(self, nums: List[int], k: int) -> int:
        # write code here
        d = {0: -1}
        res = s = 0
        for i, val in enumerate(nums):
            s += val
            if s - k in d:
                res = max(res, i - d[s - k])
            if s not in d:
                d[s] = i
        return res
