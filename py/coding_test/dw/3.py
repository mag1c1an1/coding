from collections import defaultdict

n, K = map(int, input().split())

a = list(map(int, input().split()))


d = defaultdict(int)

for v in a:
    d[v] += 1

ans = 0

end = K // 2

if K % 2 == 0:
    ans += max(0, d[K // 2] - 1)
    end -= 1

for k, v in d.items():
    if k <= end:
        s = d.get(K - k, 0)

        ans += min(v, s)
print(ans)
