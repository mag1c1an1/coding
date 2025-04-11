def sort(nums):
    n = len(nums)
    p1 = 0
    p3 = len(nums) - 1
    p2 = None
    while nums[p1] == 1 and p1 < n:
        p1 += 1

    while p3 >= 0 and nums[p3] == 3:
        p3 -= 1

    p2 = p1

    while p2 <= p3:
        if nums[p2] == 2:
            p2 += 1
        elif nums[p2] == 1:
            nums[p1], nums[p2] = nums[p2], nums[p1]
            while nums[p1] == 1 and p1 < n:
                p1 += 1
            if p2 < p1:
                p2 = p1
        else:
            nums[p2], nums[p3] = nums[p3], nums[p2]
            while nums[p3] == 3 and p3 >= 0:
                p3 -= 1
    return nums


if __name__ == "__main__":
    nums = [1, 1, 3, 3, 2, 1, 3, 2, 1]
    ans = sort(nums)
    print(ans)
