from typing import List


class Solution:

    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        for i in range(m):
            mat[i].reverse()

        ans = []
        flag = 1
        # k = i-j +n
        for k in range(1, m + n):
            min_j = max(0, n - k)
            max_j = min(n - 1, m - 1 + n - k)
            if flag:
                for j in range(max_j, min_j - 1, -1):
                    i = k + j - n
                    ans.append(mat[i][j])
            else:
                for j in range(min_j, max_j + 1):
                    i = k + j - n
                    ans.append(mat[i][j])
            flag ^= 1
        return ans
