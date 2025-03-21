class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        @cache
        def helper(i):
            if i < 0:
                return True
            x1 = False
            if i - 1 >= 0:
                x1 = helper(i - 2) and (nums[i] == nums[i - 1])
            x2 = False
            if i - 2 >= 0:
                x2 = helper(i - 3) and (
                    nums[i] == nums[i - 1] == nums[i - 2]
                    or (nums[i - 2] + 2 == nums[i - 1] + 1 == nums[i])
                )
            return x1 or x2

        return helper(len(nums) - 1)

    def validPartition_f(self, nums: List[int]) -> bool:
        n = len(nums)
        f = [True] + [False] * n
        for i, x in enumerate(nums):
            if (i > 0 and f[i - 1] and nums[i] == nums[i - 1]) or (
                i > 1
                and f[i - 2]
                and (
                    nums[i] == nums[i - 1] == nums[i - 2]
                    or nums[i] == nums[i - 1] + 1 == nums[i - 2] + 2
                )
            ):
                f[i + 1] = True
        return f[n]
