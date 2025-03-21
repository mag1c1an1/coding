class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_all = reduce(xor, nums)
        lb = xor_all & -xor_all
        ans = [0, 0]
        for x in nums:
            ans[(x & lb) != 0] ^= x
        return ans
