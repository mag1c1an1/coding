from collections import deque

m, n = map(int, input().split())

all = list(map(int, input().split()))

x, y = map(int, input().split())

for i in range(m):
    for j in range(n):
        if all[i * n + j] > 0:
            a, b = i, j

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(a, b, m, n,all):
    vis = [False] * (m * n)
    vis[a * n + b] = True
    q = deque()
    q.append((a, b))
    while q:
        u, v = q.popleft()
        cur = all[u * n + v]
        for i in range(4):
            nu, nv = u + dx[i], v + dy[i]
            if (
                0 <= nu < m
                and 0 <= nv < n
                and all[nu * n + nv] != -1
                and not vis[nu * n + nv]
            ):
                all[nu * n + nv] = cur - 1
                q.append((nu, nv))
                vis[nu * n + nv] = True

bfs(a,b,m,n,all)

print(all[x * n + y])
