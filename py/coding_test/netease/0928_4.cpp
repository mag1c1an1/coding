#include <iostream>
#include <vector>
using namespace std;
// 这道题是求考场安排最多学生人数的问题
// 给定一个 n 行 m 列的座位矩阵,其中'X'表示坏掉的座位不能坐人
// 学生可以看到左侧、右侧、左上、右上四个方向紧邻座位的答卷
// 需要安排学生使得他们无法作弊,求最大学生人数

// 使用状态压缩动态规划求解:
// f[i][j] 表示前i行,第i行状态为j时的最大学生数
// j是一个二进制数,表示第i行每个位置是否坐人(1表示坐人,0表示不坐人)

// 对于每一行的状态j:
// 1. 检查是否在坏掉的座位上放人
// 2. 检查同一行相邻位置是否都放人(不允许)
// 3. 检查与上一行的状态是否冲突(左上、右上方向)

// 最终答案是所有f[n][j]中的最大值

int main() {
  int n, m;
  cin >> n >> m;
  vector<vector<char>> g(n, vector<char>(m));
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      cin >> g[i][j];
    }
  }

  vector<vector<int>> f(n + 1, vector<int>(1 << m, -1));
  f[0][0] = 0;
  int ans = 0;
  for (int i = 1; i <= n; i++) {
    for (int j = 0; j < (1 << m); j++) {
      bool ok = true;
      string maskj;
      int tj = j;
      for (int k = 0; k < m; k++) {
        int bit = tj % 2;
        tj /= 2;
        maskj += (char)(bit + '0');
      }
      for (int k = 0; k < m; k++) {
        if (maskj[k] == '1' && g[i - 1][k] == 'X') {
          ok = false;
          break;
        }
      }
      if (!ok)
        continue;
      for (int k = 0; k < m - 1; k++) {
        if (maskj[k] == '1' && maskj[k + 1] == '1') {
          ok = false;
          break;
        }
      }

      if (!ok)
        continue;

      auto valid = [&](string mask1, string mask2) -> bool {
        for (int i = 0; i < m; i++) {
          if (mask1[i] == '1') {
            if (i > 0 && mask2[i - 1] == '1') {
              return false;
            }
            if (i + 1 < n && mask2[i + 1] == '1') {
              return false;
            }
          }
        }
        return true;
      };

      for (int mask = 0; mask < (1 << m); mask++) {
        if (f[i - 1][mask] != -1) {
          string maskk;
          int tmask = mask;
          for (int k = 0; k < m; k++) {
            int bit = tmask % 2;
            tmask /= 2;
            maskk += (char)(bit + '0');
          }
          if (valid(maskj, maskk))
            f[i][j] = max(f[i][j], f[i - 1][mask] + __builtin_popcount(j));
        }
      }
      ans = max(ans, f[i][j]);
    }
  }

  cout << ans << "\n";
}
//  64 位输出请用 printf("%lld")