def draw(grid, level, x, y):
    if level == 0:
        # print((x,y))
        grid[x][y] = "*"
        grid[x + 1][y - 1] = "*"
        grid[x + 1][y + 1] = "*"
        return
    d = 3 * (1 << (level - 1))
    draw(grid, level - 1, x, y)
    draw(grid, level - 1, x + d // 2, y - d // 2)
    draw(grid, level - 1, x + d // 2, y + d // 2)


def helper(level):
    height = 3 * (1 << (level - 1))
    width = 2 * height - 1
    grid = [[" " for _ in range(width)] for _ in range(height)]

    draw(grid, level, 0, width // 2)

    for g in grid:
        print("".join(g))

    # print
    k = width // 2
    for i in range(level):
        line = [" "] * (k + 1)
        line[-1] = "*"
        print("".join(line))


def solve():
    n = int(input())
    helper(n)


solve()
