import sys


def solve(n, m, nums):
    s = 0
    rm = [False] * m
    for num in nums:
        s += num
        if rm[s % m]:
            print(1)
            return
        else:
            rm[s % m] = True
    print(0)


for line in sys.stdin:
    n, m = map(int, line.split())
    nums = list(map(int, input().split()))
    solve(n, m, nums)
