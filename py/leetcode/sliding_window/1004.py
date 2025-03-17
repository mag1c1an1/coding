class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = l = cnt0 = 0
        for r, x in enumerate(nums):
            # cal 0
            cnt0 += 1 - x
            while cnt0 > k:
                # cal 0
                cnt0 -= 1 - nums[l]
                l += 1
            ans = max(ans, r - l + 1)
        return ans
