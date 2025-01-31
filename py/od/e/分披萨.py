n = int(input())
pisa = []
for i in range(n):
    pisa.append(int(input()))

dp = [[-1] * n for _ in range(n)]


def find(l, r):
    if dp[l][r] != -1:
        return dp[l][r]
    if pisa[l] > pisa[r]:
        l = (l + 1) % n
    else:
        r = (r - 1) % n
    if l == r:
        dp[l][r] = pisa[l]
    else:
        dp[l][r] = max(pisa[l] + find((l + 1) % n, r), pisa[r] + find(l, (r - 1)) % n)
    return dp[l][r]


ans = 0

for i in range(n):
    ans = max(ans, find((i + 1) % n, (i - 1) % n) + pisa[i])
print(ans)
