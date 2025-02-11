from collections import Counter

a, b = input().split()

c_a = Counter(a)

c_b = Counter()

l = 0

for r in range(len(b)):
    c_b[b[r]] += 1
    if r >= len(a) - 1:
        if c_a == c_b:
            print(l)
            exit()
        c_b[b[l]] -= 1
        if c_b[b[l]] == 0:
            del c_b[b[l]]
        l += 1

print(-1)
