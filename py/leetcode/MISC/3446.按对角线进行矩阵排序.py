from typing import List


class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        # k = i-j+n, 1..=m+n-1
        for k in range(1, m + n):
            min_j = max(0, n - k)
            max_j = min(n - 1, m + n - 1 - k)
            a = [grid[k + j - n][j] for j in range(min_j, max_j + 1)]
            a.sort(reverse=min_j == 0)
            for j, val in zip(range(min_j, max_j + 1), a):
                grid[k + j - n][j] = val
        return grid
