import math


t, m, n = map(int, input().split())

a = []

for _ in range(n):
    x = tuple(map(int, input().split()))
    a.append(x)

res = 0
lst = [0] * (t * 2)
a = sorted(a, key=lambda x: x[0])

for i, v in enumerate(a):
    if v[0] % 30 == 0:
        idx = v[0] // 30 -1
    else:
        idx = v[0] // 30
    if idx >= len(lst):
        continue
    lst[idx] += v[1]


pre = 0
# print(lst)

for v in lst:
    cost = pre + v
    if cost >= m:
        res += 1
        pre = cost -m
    else:
        pre = cost
print(res)
    
