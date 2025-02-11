from collections import defaultdict, deque

tree = defaultdict(list)

n = int(input())
for _ in range(n):
    child, parent = input().split()
    tree[parent].append(child)

ans = []
q = deque()
start = input()
q.append(start)
while len(q) > 0:
    nxt = q.popleft()
    for v in tree[nxt]:
        ans.append(v)
        q.append(v)

for x in sorted(ans):
    print(x)
