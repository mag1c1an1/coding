n = int(input())
nums = list(map(int, input().split()))
s = [0] * (n + 1)

for i, num in enumerate(nums):
    s[i + 1] = s[i] + num

res = -float("inf")

for i in range(n - 1):
    left_sum = s[i + 1]
    right_sum = s[n] - s[i + 1]
    res = max(res, abs(left_sum - right_sum))

print(res)
