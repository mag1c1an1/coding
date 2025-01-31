import re

s = input()
if not re.match(r"[0-9\s]+", s):
    print("[]")
    exit()

h = list(map(int, s.split()))
i = 0
j = 1
while j < len(h):
    if h[i] != h[j] and (h[i] > h[j]) != (i % 2 == 0):
        h[i], h[j] = h[j], h[i]
    i += 1
    j += 1

res = " ".join(map(str, h))
print(res)
