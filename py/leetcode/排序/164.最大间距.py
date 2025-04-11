class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        m = min(nums)
        M = max(nums)
        if M - m <= 1:
            return M - m

        n = len(nums)
        ans = d = (M - m + n - 2) // (n - 1)
        buckets = [[inf, -inf] for _ in range((M - m) // d + 1)]
        for x in nums:
            b = buckets[(x - m) // d]
            b[0] = min(b[0], x)
            b[1] = max(b[1], x)

        pre_max = inf
        for mn, mx in buckets:
            if mn != inf:
                ans = max(ans, mn - pre_max)
                pre_max = mx

        return ans
