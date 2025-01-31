import sys

grid = []

for line in sys.stdin:
    grid.append(list(map(int, line.split())))

n = len(grid)

visited = [False] * n


def dfs(s):
    visited[s] = True
    for i in range(n):
        if not visited[i] and grid[s][i] == 1:
            dfs(i)


cnt = 0

for i in range(n):
    if not visited[i]:
        cnt += 1
        dfs(i)

print(cnt)