from collections import deque

n = int(input())
nums = list(map(int, input().split()))
k = int(input())
dp = [0] * n
dq = deque()

for i in range(n):
    while dq and dq[0] < i - k:
        dq.popleft()
    dp[i] = nums[i] + (dp[dq[0]] if dq else 0)
    while dq and dp[dq[0]] <= dp[i]:
        dq.popleft()
    dq.append(i)

print(dp[-1])
