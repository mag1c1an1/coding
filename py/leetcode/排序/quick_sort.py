from typing import List
import random


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quick(nums, l, r):
            idx = random.randint(l, r)
            nums[idx], nums[l] = nums[l], nums[idx]
            pivot = nums[l]
            i, j = l, r
            while True:
                while nums[j] > pivot:
                    j -= 1
                while nums[i] < pivot:
                    i += 1
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1

                else:
                    return j

        def sort(nums, l, r):
            if l < r:
                p = quick(nums, l, r)
                sort(nums, l, p)
                sort(nums, p + 1, r)

        sort(nums, 0, len(nums) - 1)

        return nums
