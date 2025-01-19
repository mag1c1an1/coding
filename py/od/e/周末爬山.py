OFFSET = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def dfs(x, y, step, min_stop_to_height, g, m, n, k, memo, visited):
    last_height = g[x][y]

    for dx, dy in OFFSET:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue

        cur_height = g[nx][ny]
        if abs(cur_height - last_height) <= k:
            step += 1
            if (
                cur_height not in min_stop_to_height
                or step < min_stop_to_height[cur_height]
            ):
                min_stop_to_height[cur_height] = step
            if memo[nx][ny] == 0 or memo[nx][ny] > step:
                memo[nx][ny] = step
                visited[nx][ny] = True
                dfs(nx, ny, step, min_stop_to_height, g, m, n, k, memo, visited)
                visited[nx][ny] = False
            step -= 1


def main():
    m, n, k = map(int, input().split())

    g = [list(map(int, input().split())) for _ in range(m)]

    min_step_to_height = {g[0][0]: 0}
    memo = [[0] * n for _ in range(m)]
    vis = [[False for _ in range(n)] for _ in range(m)]

    dfs(0, 0, 0, min_step_to_height, g, m, n, k, memo, vis)
    mh = max(min_step_to_height.keys())
    ms = min_step_to_height[mh]

    print(f"{mh} {ms}")


if __name__ == "__main__":
    main()
